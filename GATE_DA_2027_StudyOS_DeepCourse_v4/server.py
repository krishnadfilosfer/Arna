"""GATE DA StudyOS: account-based, SQLite-backed study website.

Python standard library only. Deploy behind HTTPS reverse proxy and attach a
persistent writable disk to STUDYOS_DATA_DIR when using public hosting.
"""
import argparse
import getpass
import hashlib
import hmac
import json
import math
import os
import re
import secrets
import sqlite3
import threading
import time
from collections import defaultdict, deque
from datetime import datetime, timedelta, timezone
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, unquote

BASE = Path(__file__).resolve().parent
CONTENT = json.loads((BASE/'content.json').read_text(encoding='utf-8'))
LESSONS = {x['id']: x for x in CONTENT['lessons']}
DAYS = {x['date']: x for x in CONTENT['days']}
QUESTIONS = {x['id']: x for x in CONTENT['questions']}
PUBLIC_CONTENT = {**CONTENT, 'questions': [{k:v for k,v in q.items() if k not in ('answer','solution')} for q in CONTENT['questions']]}
DATA_DIR = Path(os.environ.get('STUDYOS_DATA_DIR', str(BASE/'data'))).expanduser().resolve()
DATA_DIR.mkdir(parents=True, exist_ok=True)
DBPATH = DATA_DIR/'accounts.sqlite3'
LOCK = threading.RLock()
IST = timezone(timedelta(hours=5, minutes=30))
COOKIE = 'studyos_session'
SESSION_SECONDS = 30 * 86400
SECURE_COOKIES = os.environ.get('STUDYOS_SECURE_COOKIES', '0') == '1'
ALLOW_SIGNUPS = os.environ.get('STUDYOS_ALLOW_SIGNUPS', '1') == '1'
AUTH_ATTEMPTS = defaultdict(deque)


def now(): return datetime.now(IST).isoformat(timespec='seconds')
def today(): return datetime.now(IST).date().isoformat()
def connect():
    db = sqlite3.connect(DBPATH, timeout=15)
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA foreign_keys=ON')
    db.execute('PRAGMA busy_timeout=15000')
    return db


def init_db():
    with LOCK, connect() as db:
        db.executescript('''
            PRAGMA journal_mode=WAL;
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE COLLATE NOCASE,
                display_name TEXT NOT NULL,
                password_salt TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL,
                active INTEGER NOT NULL DEFAULT 1
            );
            CREATE TABLE IF NOT EXISTS sessions(
                token_hash TEXT PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                csrf_token TEXT NOT NULL,
                expires_at INTEGER NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_sessions_user ON sessions(user_id);
            CREATE TABLE IF NOT EXISTS topics(user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE, id TEXT NOT NULL, completed INTEGER NOT NULL, updated_at TEXT NOT NULL, PRIMARY KEY(user_id,id));
            CREATE TABLE IF NOT EXISTS day_tasks(user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE, day TEXT NOT NULL, task TEXT NOT NULL, completed INTEGER NOT NULL, updated_at TEXT NOT NULL, PRIMARY KEY(user_id,day,task));
            CREATE TABLE IF NOT EXISTS notes(user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE, topic_id TEXT NOT NULL, content TEXT NOT NULL, updated_at TEXT NOT NULL, PRIMARY KEY(user_id,topic_id));
            CREATE TABLE IF NOT EXISTS quiz_attempts(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE, timestamp TEXT NOT NULL, day TEXT, label TEXT, num_questions INTEGER NOT NULL, correct INTEGER NOT NULL, score REAL NOT NULL, max_score REAL NOT NULL, results_json TEXT NOT NULL);
            CREATE INDEX IF NOT EXISTS idx_attempt_user ON quiz_attempts(user_id,id);
            CREATE TABLE IF NOT EXISTS activity(user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE, day TEXT NOT NULL, last_at TEXT NOT NULL, PRIMARY KEY(user_id,day));
            CREATE TABLE IF NOT EXISTS recalls(user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE, topic_id TEXT NOT NULL, rating TEXT NOT NULL, updated_at TEXT NOT NULL, due_date TEXT NOT NULL, interval_days INTEGER NOT NULL, repetitions INTEGER NOT NULL, PRIMARY KEY(user_id,topic_id));
            CREATE TABLE IF NOT EXISTS settings(user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE, key TEXT NOT NULL, value TEXT NOT NULL, PRIMARY KEY(user_id,key));
        ''')
        db.commit()


def hash_password(password, salt=None):
    salt = salt or secrets.token_bytes(16)
    derived = hashlib.scrypt(password.encode('utf-8'), salt=salt, n=2**14, r=8, p=1, dklen=32)
    return salt.hex(), derived.hex()


def authenticate(username, password):
    with connect() as db:
        row = db.execute('SELECT * FROM users WHERE username=? COLLATE NOCASE AND active=1', (username,)).fetchone()
    if row:
        try: attempted = hash_password(password, bytes.fromhex(row['password_salt']))[1]
        except ValueError: return None
        if hmac.compare_digest(attempted, row['password_hash']): return row
    else:
        # Equalize computational cost when the username is unknown.
        hash_password(password, b'\x01'*16)
    return None


def create_session(db, uid):
    raw = secrets.token_urlsafe(36)
    csrf = secrets.token_urlsafe(32)
    db.execute('DELETE FROM sessions WHERE expires_at < ?', (int(time.time()),))
    db.execute('INSERT INTO sessions VALUES(?,?,?,?)', (hashlib.sha256(raw.encode()).hexdigest(), uid, csrf, int(time.time())+SESSION_SECONDS))
    return raw, csrf


def touch(db, uid):
    db.execute('INSERT INTO activity(user_id,day,last_at) VALUES(?,?,?) ON CONFLICT(user_id,day) DO UPDATE SET last_at=excluded.last_at', (uid,today(),now()))


def public_progress(uid):
    with connect() as db:
        ts = {r['id']:bool(r['completed']) for r in db.execute('SELECT id,completed FROM topics WHERE user_id=?',(uid,))}
        dt = {}
        for r in db.execute('SELECT day,task,completed FROM day_tasks WHERE user_id=?',(uid,)):
            dt.setdefault(r['day'],{})[r['task']] = bool(r['completed'])
        notes = {r['topic_id']:r['content'] for r in db.execute('SELECT topic_id,content FROM notes WHERE user_id=?',(uid,))}
        recalls = {r['topic_id']:{'rating':r['rating'],'due_date':r['due_date'],'interval_days':r['interval_days'],'repetitions':r['repetitions']} for r in db.execute('SELECT * FROM recalls WHERE user_id=?',(uid,))}
        recent = [{k:r[k] for k in ('id','timestamp','day','label','num_questions','correct','score','max_score')} for r in db.execute('SELECT * FROM quiz_attempts WHERE user_id=? ORDER BY id DESC LIMIT 30',(uid,))]
        settings = {'daily_minutes':'150',**{r['key']:r['value'] for r in db.execute('SELECT key,value FROM settings WHERE user_id=?',(uid,))}}
        active = {r['day'] for r in db.execute('SELECT day FROM activity WHERE user_id=?',(uid,))}
        counts = {r['day']:r['total'] for r in db.execute('SELECT day,COUNT(*) AS total FROM quiz_attempts WHERE user_id=? AND day IS NOT NULL GROUP BY day',(uid,))}
        wrong = {}
        for r in db.execute('SELECT results_json FROM quiz_attempts WHERE user_id=? ORDER BY id DESC LIMIT 60',(uid,)):
            for item in json.loads(r['results_json']):
                s = item['subject']; t = wrong.setdefault(s,{'right':0,'attempted':0})
                if item['answered']: t['attempted']+=1; t['right']+=int(item['correct'])
        ref = datetime.now(IST).date()
        if ref.isoformat() not in active:ref-=timedelta(days=1)
        streak = 0
        while ref.isoformat() in active:
            streak+=1;ref-=timedelta(days=1)
    return {'topics':ts,'day_tasks':dt,'notes':notes,'recalls':recalls,'recent_attempts':recent,'settings':settings,'active_days':sorted(active),'quiz_count_by_day':counts,'subject_accuracy':wrong,'streak':streak}


def grade(q, answer):
    if answer is None or answer=='':return False,False
    try:
        if q['type']=='NAT':
            val=float(answer)
            return math.isfinite(val), math.isfinite(val) and abs(val-q['answer'])<=max(.005,abs(q['answer'])*.001)
        if q['type']=='MCQ':return True, int(answer)==q['answer']
        if q['type']=='MSQ':
            if not isinstance(answer,list):return False,False
            vals=[int(x) for x in answer]
            if len(set(vals))!=len(vals) or any(x not in (0,1,2,3) for x in vals):return False,False
            return True,sorted(vals)==sorted(q['answer'])
    except (TypeError,ValueError,OverflowError):return False,False
    return False,False


def too_many(ip, operation, limit, interval):
    key = (ip,operation)
    with LOCK:
        d = AUTH_ATTEMPTS[key]
        curr = time.monotonic()
        while d and d[0] < curr-interval: d.popleft()
        if len(d)>=limit:return True
        d.append(curr)
    return False


class Handler(BaseHTTPRequestHandler):
    server_version='StudyOS/3.0'
    def log_message(self,format,*args):print('%s - %s'%(self.address_string(),format%args))
    def send(self,status,data,ctype='application/json',filename=None,cookie=None):
        if isinstance(data,(dict,list)):body=json.dumps(data,ensure_ascii=False).encode('utf-8')
        elif isinstance(data,str):body=data.encode('utf-8')
        else:body=data
        self.send_response(status)
        self.send_header('Content-Type',ctype+('; charset=utf-8' if 'text/' in ctype or 'json' in ctype else ''))
        self.send_header('Content-Length',str(len(body)))
        self.send_header('X-Content-Type-Options','nosniff')
        self.send_header('Referrer-Policy','same-origin')
        self.send_header('X-Frame-Options','DENY')
        self.send_header('Cache-Control','no-store')
        self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; form-action 'self'; object-src 'none'; base-uri 'none'")
        if SECURE_COOKIES:self.send_header('Strict-Transport-Security','max-age=31536000; includeSubDomains')
        if cookie is not None:
            self.send_header('Set-Cookie', f'{COOKIE}={cookie}; Path=/; HttpOnly; SameSite=Strict; Max-Age={SESSION_SECONDS if cookie else 0}'+('; Secure' if SECURE_COOKIES else ''))
        if filename:self.send_header('Content-Disposition',f'attachment; filename="{filename}"')
        self.end_headers();self.wfile.write(body)
    def current_session(self):
        cookie=SimpleCookie()
        try:cookie.load(self.headers.get('Cookie',''))
        except Exception:return None
        if COOKIE not in cookie:return None
        raw=cookie[COOKIE].value
        if len(raw)>128:return None
        with connect() as db:
            r=db.execute('SELECT s.token_hash,s.csrf_token,s.user_id,u.username,u.display_name FROM sessions s JOIN users u ON u.id=s.user_id WHERE s.token_hash=? AND s.expires_at>? AND u.active=1',(hashlib.sha256(raw.encode()).hexdigest(),int(time.time()))).fetchone()
        return r
    def same_origin(self):
        if self.headers.get('Sec-Fetch-Site','') in ('cross-site','same-site'):return False
        origin=self.headers.get('Origin')
        if origin:
            try:
                u=urlsplit(origin)
                if u.netloc.lower()!=self.headers.get('Host','').lower() or u.scheme not in ('https','http'):return False
            except ValueError:return False
        return True
    def require_auth(self, session):
        if not session:self.send(401,{'error':'Please log in first.','code':'AUTH_REQUIRED'});return False
        return True
    def read_json(self):
        if self.headers.get('Content-Type','').split(';')[0].strip().lower()!='application/json':raise ValueError('Expected application/json')
        try:
            length=int(self.headers.get('Content-Length','0'))
            if length<1 or length>3_000_000:raise ValueError('Payload must be 1 B to 3 MB')
            obj=json.loads(self.rfile.read(length))
            if not isinstance(obj,dict):raise ValueError('Expected a JSON object')
            return obj
        except (ValueError,json.JSONDecodeError) as exc:raise ValueError(str(exc))
    def do_GET(self):
        path=unquote(urlsplit(self.path).path)
        if path=='/api/health':return self.send(200,{'ok':True,'date':today(),'lessons':len(LESSONS),'questions':len(QUESTIONS),'days':len(DAYS)})
        if path=='/api/me':
            s=self.current_session()
            return self.send(200,{'authenticated':bool(s),'user':{'username':s['username'],'display_name':s['display_name']} if s else None,'csrf_token':s['csrf_token'] if s else None,'registration_enabled':ALLOW_SIGNUPS})
        if path.startswith('/api/'):
            s=self.current_session()
            if not self.require_auth(s):return
            uid=s['user_id']
            if path=='/api/bootstrap':return self.send(200,{'content':PUBLIC_CONTENT,'progress':public_progress(uid),'server_date':today()})
            if path=='/api/export':
                with connect() as db:
                    cols={
                        'topics':'id,completed,updated_at',
                        'day_tasks':'day,task,completed,updated_at',
                        'notes':'topic_id,content,updated_at',
                        'quiz_attempts':'timestamp,day,label,num_questions,correct,score,max_score,results_json',
                        'activity':'day,last_at',
                        'settings':'key,value',
                        'recalls':'topic_id,rating,updated_at,due_date,interval_days,repetitions'
                    }
                    result={'version':1,'exported_at':now(), 'username':s['username']}
                    for tbl,col in cols.items():result[tbl]=[dict(r) for r in db.execute(f'SELECT {col} FROM {tbl} WHERE user_id=?',(uid,))]
                return self.send(200,result,filename=f"studyos_backup_{s['username']}.json")
            return self.send(404,{'error':'Unknown API route'})
        if path=='/':path='/static/index.html'
        if not path.startswith('/static/'):return self.send(404,{'error':'Not found'})
        root=(BASE/'static').resolve();target=(BASE/path.lstrip('/')).resolve()
        if not target.is_relative_to(root) or not target.is_file():return self.send(404,{'error':'Not found'})
        typ={'.html':'text/html','.css':'text/css','.js':'text/javascript','.svg':'image/svg+xml','.png':'image/png','.ico':'image/x-icon'}.get(target.suffix,'application/octet-stream')
        return self.send(200,target.read_bytes(),typ)
    def do_POST(self):
        try:self.handle_post()
        except (ValueError,KeyError,TypeError,sqlite3.IntegrityError) as exc:self.send(400,{'error':str(exc)[:200]})
        except Exception as exc:
            print('Server error:',repr(exc));self.send(500,{'error':'Internal server error; inspect server console'})
    def handle_post(self):
        path=urlsplit(self.path).path
        if not self.same_origin():return self.send(403,{'error':'Cross-origin request blocked'})
        obj=self.read_json()
        if path in ('/api/register','/api/login'):
            if too_many(self.client_address[0],path,100 if path.endswith('login') else 20,600):return self.send(429,{'error':'Too many attempts. Please try later.'})
            username=obj.get('username','');password=obj.get('password','')
            if not isinstance(username,str) or not isinstance(password,str):raise ValueError('Enter a username and password')
            username=username.lower().strip()
            if path=='/api/register':
                if not ALLOW_SIGNUPS:return self.send(403,{'error':'New registrations are currently disabled'})
                display_name=obj.get('display_name','')
                if not re.fullmatch(r'[a-z0-9_]{3,24}',username):raise ValueError('Username must be 3–24 letters, numbers, or underscores')
                if not isinstance(display_name,str) or not 1<=len(display_name.strip())<=40:raise ValueError('Display name must be 1–40 characters')
                if not 10<=len(password)<=128:raise ValueError('Password must be 10–128 characters')
                salt,digest=hash_password(password)
                with LOCK,connect() as db:
                    if db.execute('SELECT 1 FROM users WHERE username=? COLLATE NOCASE',(username,)).fetchone():return self.send(409,{'error':'Username already taken'})
                    cur=db.execute('INSERT INTO users(username,display_name,password_salt,password_hash,created_at) VALUES (?,?,?,?,?)',(username,display_name.strip(),salt,digest,now()))
                    uid=cur.lastrowid
                    db.execute('INSERT INTO settings VALUES (?,?,?)',(uid,'daily_minutes','150'))
                    raw,csrf=create_session(db,uid)
                    db.commit()
                return self.send(201,{'ok':True,'user':{'username':username,'display_name':display_name.strip()},'csrf_token':csrf},cookie=raw)
            if not username or not password or len(password)>128:raise ValueError('Enter a valid username and password')
            if too_many(self.client_address[0], 'failed:'+username, 12,600):return self.send(429,{'error':'Too many sign-in attempts for this account. Try later.'})
            user=authenticate(username,password)
            if not user:return self.send(401,{'error':'Incorrect username or password'})
            with LOCK,connect() as db:
                raw,csrf=create_session(db,user['id']);db.commit()
            return self.send(200,{'ok':True,'user':{'username':user['username'],'display_name':user['display_name']},'csrf_token':csrf},cookie=raw)
        s=self.current_session()
        if not self.require_auth(s):return
        if not hmac.compare_digest(self.headers.get('X-CSRF-Token',''),s['csrf_token']):return self.send(403,{'error':'Invalid session protection token. Refresh and try again.'})
        uid=s['user_id']
        if path=='/api/logout':
            with LOCK, connect() as db:
                db.execute('DELETE FROM sessions WHERE token_hash=?',(s['token_hash'],));db.commit()
            return self.send(200,{'ok':True},cookie='')
        if path=='/api/change-password':
            old=obj.get('old_password','');new=obj.get('new_password','')
            if not isinstance(old,str) or not isinstance(new,str) or not 10<=len(new)<=128:raise ValueError('New password must be 10–128 characters')
            if not authenticate(s['username'],old):return self.send(403,{'error':'Current password is incorrect'})
            salt,digest=hash_password(new)
            with LOCK,connect() as db:
                db.execute('UPDATE users SET password_salt=?, password_hash=? WHERE id=?',(salt,digest,uid))
                db.execute('DELETE FROM sessions WHERE user_id=? AND token_hash<>?',(uid,s['token_hash']))
                db.commit()
            return self.send(200,{'ok':True})
        if path=='/api/topic':
            ident=obj.get('id');complete=obj.get('completed')
            if ident not in LESSONS or type(complete)!=bool:raise ValueError('Invalid topic ID or completed flag')
            with LOCK,connect() as db:
                db.execute('INSERT INTO topics VALUES(?,?,?,?) ON CONFLICT(user_id,id) DO UPDATE SET completed=excluded.completed,updated_at=excluded.updated_at',(uid,ident,int(complete),now()))
                touch(db,uid);db.commit()
            return self.send(200,{'ok':True,'id':ident,'completed':complete})
        if path=='/api/day':
            day=obj.get('day');task=obj.get('task');complete=obj.get('completed')
            if day not in DAYS or task not in ('read','practice','recall') or type(complete)!=bool:raise ValueError('Invalid date/task/flag')
            with LOCK,connect() as db:
                db.execute('INSERT INTO day_tasks VALUES(?,?,?,?,?) ON CONFLICT(user_id,day,task) DO UPDATE SET completed=excluded.completed,updated_at=excluded.updated_at',(uid,day,task,int(complete),now()))
                touch(db,uid);db.commit()
            return self.send(200,{'ok':True,'day':day,'task':task,'completed':complete})
        if path=='/api/note':
            ident=obj.get('id');value=obj.get('text')
            if ident not in LESSONS or not isinstance(value,str) or len(value)>8000:raise ValueError('Invalid topic or note over 8000 characters')
            with LOCK,connect() as db:
                db.execute('INSERT INTO notes VALUES(?,?,?,?) ON CONFLICT(user_id,topic_id) DO UPDATE SET content=excluded.content,updated_at=excluded.updated_at',(uid,ident,value,now()))
                touch(db,uid);db.commit()
            return self.send(200,{'ok':True})
        if path=='/api/recall':
            ident=obj.get('id');rating=obj.get('rating')
            if ident not in LESSONS or rating not in ('again','hard','good','easy'):raise ValueError('Invalid flashcard or rating')
            with LOCK,connect() as db:
                old=db.execute('SELECT interval_days,repetitions FROM recalls WHERE user_id=? AND topic_id=?',(uid,ident)).fetchone()
                prev=old['interval_days'] if old else 0;reps=old['repetitions'] if old else 0
                if rating=='again':interval,reps=1,0
                elif rating=='hard':interval,reps=max(2,round(max(1,prev)*1.3)),reps+1
                elif rating=='good':interval,reps=max(3,round(max(1,prev)*2.2)),reps+1
                else:interval,reps=max(5,round(max(1,prev)*3)),reps+1
                due=(datetime.now(IST).date()+timedelta(days=interval)).isoformat()
                db.execute('INSERT INTO recalls VALUES(?,?,?,?,?,?,?) ON CONFLICT(user_id,topic_id) DO UPDATE SET rating=excluded.rating,updated_at=excluded.updated_at,due_date=excluded.due_date,interval_days=excluded.interval_days,repetitions=excluded.repetitions',(uid,ident,rating,now(),due,interval,reps))
                touch(db,uid);db.commit()
            return self.send(200,{'ok':True,'id':ident,'rating':rating,'due_date':due,'interval_days':interval,'repetitions':reps})
        if path=='/api/setting':
            if obj.get('key')!='daily_minutes':raise ValueError('Unknown setting')
            try: val=int(obj.get('value'))
            except (TypeError,ValueError,OverflowError):raise ValueError('Daily minutes must be a number')
            if not 45<=val<=480:raise ValueError('Target minutes must be between 45 and 480')
            with LOCK,connect() as db:
                db.execute('INSERT INTO settings VALUES(?,?,?) ON CONFLICT(user_id,key) DO UPDATE SET value=excluded.value',(uid,'daily_minutes',str(val)))
                touch(db,uid);db.commit()
            return self.send(200,{'ok':True})
        if path=='/api/quiz':
            answers=obj.get('answers');day=obj.get('day');label=obj.get('label','Daily drill')
            if not isinstance(answers,dict) or not 1<=len(answers)<=65:raise ValueError('Submit 1 to 65 questions')
            if day is not None and day not in DAYS:raise ValueError('Unknown day')
            if not isinstance(label,str) or len(label)>90:raise ValueError('Invalid label')
            results=[];score=0.;maxscore=0.;correct=0
            for ident,value in answers.items():
                if ident not in QUESTIONS:raise ValueError(f'Invalid question {ident}')
                q=QUESTIONS[ident];answered,good=grade(q,value);mark=q['marks']
                obtained=mark if good else (-(mark/3) if answered and q['type']=='MCQ' else 0)
                score+=obtained;maxscore+=mark;correct+=int(good)
                results.append({'id':ident,'subject':q['subject'],'lesson_id':q['lesson_id'],'prompt':q['prompt'],'answered':answered,'your_answer':value,'correct':good,'correct_answer':q['answer'],'solution':q['solution'],'marks':mark,'awarded':round(obtained,4),'type':q['type']})
            with LOCK,connect() as db:
                cur=db.execute('INSERT INTO quiz_attempts(user_id,timestamp,day,label,num_questions,correct,score,max_score,results_json) VALUES(?,?,?,?,?,?,?,?,?)',(uid,now(),day,label,len(results),correct,score,maxscore,json.dumps(results,ensure_ascii=False)))
                for result in results:
                    if result['answered'] and not result['correct']:
                        db.execute('INSERT INTO recalls VALUES(?,?,?,?,?,?,?) ON CONFLICT(user_id,topic_id) DO UPDATE SET rating=excluded.rating,updated_at=excluded.updated_at,due_date=excluded.due_date,interval_days=excluded.interval_days,repetitions=excluded.repetitions',(uid,result['lesson_id'],'again',now(),today(),0,0))
                touch(db,uid);db.commit();attempt_id=cur.lastrowid
            return self.send(200,{'ok':True,'attempt_id':attempt_id,'correct':correct,'score':round(score,2),'max_score':maxscore,'results':results})
        if path=='/api/import':
            payload=obj.get('backup')
            if not isinstance(payload,dict) or payload.get('version')!=1:raise ValueError('Invalid backup version')
            required=('topics','day_tasks','notes','quiz_attempts','activity','settings')
            if any(not isinstance(payload.get(t),list) for t in required):raise ValueError('Missing backup table')
            if any(not isinstance(payload.get(t,[]),list) for t in ('recalls',)):raise ValueError('Malformed recalls')
            if sum(len(payload.get(t,[])) for t in (*required,'recalls'))>12000:raise ValueError('Backup contains too many records')
            for t in payload['topics']:
                if not isinstance(t,dict) or t.get('id') not in LESSONS or t.get('completed') not in (0,1):raise ValueError('Invalid topic in backup')
            for t in payload['day_tasks']:
                if not isinstance(t,dict) or t.get('day') not in DAYS or t.get('task') not in ('read','practice','recall') or t.get('completed') not in (0,1):raise ValueError('Invalid day in backup')
            for t in payload['notes']:
                if not isinstance(t,dict) or t.get('topic_id') not in LESSONS or not isinstance(t.get('content'),str) or len(t['content'])>8000:raise ValueError('Invalid note in backup')
            for t in payload.get('recalls',[]):
                if not isinstance(t,dict) or t.get('topic_id') not in LESSONS or t.get('rating') not in ('again','hard','good','easy'):raise ValueError('Invalid flashcard in backup')
            with LOCK,connect() as db:
                for tbl in ('topics','day_tasks','notes','quiz_attempts','activity','settings','recalls'):db.execute(f'DELETE FROM {tbl} WHERE user_id=?',(uid,))
                for t in payload['topics']:db.execute('INSERT INTO topics VALUES(?,?,?,?)',(uid,t['id'],t['completed'],t.get('updated_at',now())))
                for t in payload['day_tasks']:db.execute('INSERT INTO day_tasks VALUES(?,?,?,?,?)',(uid,t['day'],t['task'],t['completed'],t.get('updated_at',now())))
                for t in payload['notes']:db.execute('INSERT INTO notes VALUES(?,?,?,?)',(uid,t['topic_id'],t['content'],t.get('updated_at',now())))
                for t in payload['quiz_attempts']:
                    db.execute('INSERT INTO quiz_attempts(user_id,timestamp,day,label,num_questions,correct,score,max_score,results_json) VALUES(?,?,?,?,?,?,?,?,?)',(uid,t['timestamp'],t.get('day'),t['label'],int(t['num_questions']),int(t['correct']),float(t['score']),float(t['max_score']),t['results_json']))
                for t in payload['activity']:db.execute('INSERT INTO activity VALUES(?,?,?)',(uid,t['day'],t['last_at']))
                for t in payload.get('recalls',[]):db.execute('INSERT INTO recalls VALUES(?,?,?,?,?,?,?)',(uid,t['topic_id'],t['rating'],t['updated_at'],t['due_date'],int(t['interval_days']),int(t['repetitions'])))
                for t in payload['settings']:
                    if t.get('key')=='daily_minutes' and 45<=int(t['value'])<=480:db.execute('INSERT INTO settings VALUES(?,?,?)',(uid,'daily_minutes',str(t['value'])))
                db.execute('INSERT OR IGNORE INTO settings VALUES(?,?,?)',(uid,'daily_minutes','150'))
                touch(db,uid);db.commit()
            return self.send(200,{'ok':True,'progress':public_progress(uid)})
        if path=='/api/reset':
            if obj.get('confirm')!='RESET':raise ValueError('Type RESET to confirm')
            with LOCK,connect() as db:
                for tbl in ('topics','day_tasks','notes','quiz_attempts','activity','recalls'):db.execute(f'DELETE FROM {tbl} WHERE user_id=?',(uid,))
                db.commit()
            return self.send(200,{'ok':True,'progress':public_progress(uid)})
        return self.send(404,{'error':'Unknown API route'})


def cli():
    parser=argparse.ArgumentParser(description='GATE DA StudyOS — private accounts & study progress')
    parser.add_argument('--host',default=os.environ.get('HOST','127.0.0.1'),help='Use 0.0.0.0 for hosting behind HTTPS')
    parser.add_argument('--port',type=int,default=int(os.environ.get('PORT','8765')))
    parser.add_argument('--list-users',action='store_true')
    parser.add_argument('--reset-user-password',metavar='USERNAME')
    parser.add_argument('--disable-user',metavar='USERNAME')
    parser.add_argument('--enable-user',metavar='USERNAME')
    args=parser.parse_args()
    init_db()
    if args.list_users:
        with connect() as db:
            for row in db.execute('SELECT username,display_name,active,created_at FROM users ORDER BY created_at'):
                print(f"{row['username']:<24} {row['display_name']:<40} {'active' if row['active'] else 'disabled':<9} {row['created_at']}")
        return
    if args.disable_user or args.enable_user:
        user=args.disable_user or args.enable_user
        enabled=int(bool(args.enable_user))
        with LOCK,connect() as db:
            cur=db.execute('UPDATE users SET active=? WHERE username=? COLLATE NOCASE',(enabled,user))
            if cur.rowcount!=1:raise SystemExit('No such account')
            if not enabled:
                uid=db.execute('SELECT id FROM users WHERE username=? COLLATE NOCASE',(user,)).fetchone()['id']
                db.execute('DELETE FROM sessions WHERE user_id=?',(uid,))
            db.commit()
        print(f'Account {user}: {"enabled" if enabled else "disabled"}')
        return
    if args.reset_user_password:
        pw=getpass.getpass('New password (10+ characters): ')
        if not 10<=len(pw)<=128:raise SystemExit('Password must be 10–128 characters')
        salt,digest=hash_password(pw)
        with LOCK,connect() as db:
            cur=db.execute('UPDATE users SET password_salt=?,password_hash=? WHERE username=? COLLATE NOCASE',(salt,digest,args.reset_user_password))
            if cur.rowcount!=1:raise SystemExit('No such account')
            uid=db.execute('SELECT id FROM users WHERE username=? COLLATE NOCASE',(args.reset_user_password,)).fetchone()['id']
            db.execute('DELETE FROM sessions WHERE user_id=?',(uid,));db.commit()
        print('Password changed; all sessions invalidated.')
        return
    if args.host not in ('localhost','127.0.0.1','::1') and not SECURE_COOKIES:
        print('WARNING: You are using a public bind. Set STUDYOS_SECURE_COOKIES=1 and put the app behind HTTPS before inviting users.')
    srv=ThreadingHTTPServer((args.host,args.port),Handler)
    print(f'\nGATE DA StudyOS: http://{args.host}:{args.port}\nPrivate progress DB: {DBPATH}\nSign-ups: {"on" if ALLOW_SIGNUPS else "off"}\nPress Ctrl+C to stop.\n')
    try:srv.serve_forever()
    except KeyboardInterrupt:pass
    finally:srv.server_close()

if __name__=='__main__':cli()
