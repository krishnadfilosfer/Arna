"""Integration checks for private account data, backup/restore, and sessions.
Run: python -m unittest discover -s tests -v
"""
import http.cookiejar
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from urllib.error import HTTPError
from urllib.request import Request, build_opener, HTTPCookieProcessor

ROOT=Path(__file__).resolve().parents[1]

class MultiuserIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory()
        sock=socket.socket();sock.bind(('127.0.0.1',0));cls.port=sock.getsockname()[1];sock.close()
        cls.base=f'http://127.0.0.1:{cls.port}'
        env={**os.environ,'STUDYOS_DATA_DIR':cls.tmp.name, 'STUDYOS_SECURE_COOKIES':'0','STUDYOS_ALLOW_SIGNUPS':'1'}
        cls.proc=subprocess.Popen([sys.executable,'server.py','--host','127.0.0.1','--port',str(cls.port)],cwd=ROOT,env=env,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
        for _ in range(60):
            try:
                from urllib.request import urlopen
                if json.load(urlopen(cls.base+'/api/health',timeout=1))['ok']:break
            except Exception:time.sleep(.15)
        else:raise RuntimeError('Server failed to start')
    @classmethod
    def tearDownClass(cls):
        cls.proc.terminate();cls.proc.wait(timeout=5);cls.tmp.cleanup()
    def opener(self):return build_opener(HTTPCookieProcessor(http.cookiejar.CookieJar()))
    def req(self,opener,path,data=None,csrf=None):
        headers={}
        if data is not None:headers['Content-Type']='application/json'
        if csrf is not None:headers['X-CSRF-Token']=csrf
        try:
            with opener.open(Request(self.base+path,headers=headers,data=json.dumps(data).encode() if data is not None else None),timeout=8) as r:
                return r.status,json.load(r)
        except HTTPError as e:
            return e.code,json.load(e)
    def test_user_isolation_backup_and_security(self):
        a=self.opener();b=self.opener();anon=self.opener()
        self.assertEqual(401,self.req(anon,'/api/bootstrap')[0])
        r,ad=self.req(a,'/api/register',{'username':'first_learner','display_name':'First Student','password':'strong-passphrase-123'})
        self.assertEqual(201,r);token_a=ad['csrf_token']
        r,bd=self.req(b,'/api/register',{'username':'second_learner','display_name':'Second Student','password':'second-passphrase-456'})
        self.assertEqual(201,r);token_b=bd['csrf_token']
        self.assertEqual(403,self.req(a,'/api/topic',{'id':'PS-001','completed':True})[0]) # no CSRF
        for endpoint,payload in [('/api/topic',{'id':'PS-001','completed':True}),('/api/note',{'id':'PS-001','text':'Personal first-user note'}),('/api/day',{'day':'2026-11-05','task':'read','completed':True}),('/api/recall',{'id':'PS-001','rating':'good'}),('/api/setting',{'key':'daily_minutes','value':210})]:
            status,_=self.req(a,endpoint,payload,token_a)
            self.assertEqual(200,status,(endpoint,status))
        # The question keys come from the authenticated course content.
        question_id=self.req(a,'/api/bootstrap')[1]['content']['questions'][0]['id']
        status,attempt=self.req(a,'/api/quiz',{'answers':{question_id:0},'day':'2026-11-05','label':'Test quiz'},token_a)
        self.assertEqual(200,status);self.assertEqual(1,len(attempt['results']))
        aa=self.req(a,'/api/bootstrap')[1]['progress'];bb=self.req(b,'/api/bootstrap')[1]['progress']
        self.assertTrue(aa['topics']['PS-001']);self.assertNotIn('PS-001',bb['topics'])
        self.assertEqual('Personal first-user note',aa['notes']['PS-001']);self.assertEqual({},bb['notes'])
        self.assertEqual(1,len(aa['recent_attempts']));self.assertEqual(0,len(bb['recent_attempts']))
        self.assertEqual('210',aa['settings']['daily_minutes']);self.assertEqual('150',bb['settings']['daily_minutes'])
        export=self.req(a,'/api/export')[1]
        self.assertEqual('first_learner',export['username']);self.assertEqual(1,len(export['quiz_attempts']))
        self.assertEqual(200,self.req(a,'/api/reset',{'confirm':'RESET'},token_a)[0]);self.assertEqual({},self.req(a,'/api/bootstrap')[1]['progress']['topics'])
        self.assertEqual(200,self.req(a,'/api/import',{'backup':export},token_a)[0])
        self.assertTrue(self.req(a,'/api/bootstrap')[1]['progress']['topics']['PS-001'])
        self.assertEqual({},self.req(b,'/api/bootstrap')[1]['progress']['topics'])
        self.assertEqual(200,self.req(a,'/api/change-password',{'old_password':'strong-passphrase-123','new_password':'new-strong-passphrase-321'},token_a)[0])
        self.assertEqual(200,self.req(a,'/api/logout',{},token_a)[0]);self.assertEqual(401,self.req(a,'/api/bootstrap')[0])
        self.assertEqual(401,self.req(a,'/api/login',{'username':'first_learner','password':'strong-passphrase-123'})[0])
        self.assertEqual(200,self.req(a,'/api/login',{'username':'first_learner','password':'new-strong-passphrase-321'})[0])
        c=self.opener()  # Represents another phone or laptop signed into the same account.
        status,c_login=self.req(c,'/api/login',{'username':'first_learner','password':'new-strong-passphrase-321'})
        self.assertEqual(200,status)
        self.assertTrue(self.req(c,'/api/bootstrap')[1]['progress']['topics']['PS-001'])
        self.assertEqual(401,self.req(anon,'/api/export')[0])
        self.assertEqual('Personal first-user note',self.req(a,'/api/bootstrap')[1]['progress']['notes']['PS-001'])
        self.assertEqual(404,self.req(a,'/data/accounts.sqlite3')[0])

if __name__=='__main__': unittest.main()
