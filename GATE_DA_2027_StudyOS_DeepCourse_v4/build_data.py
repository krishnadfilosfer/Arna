"""Build an editable syllabus content pack, 89-day curriculum and original question bank."""
from collections import Counter, defaultdict
from datetime import date, timedelta
from pathlib import Path
import json, random, re

ROOT=Path(__file__).parent
SUBJECTS=[
    ('PS','Probability & Statistics','Probabilities, estimation and inference','#4c7de5'),
    ('LA','Linear Algebra','Vectors, matrices and decompositions','#8e6bdc'),
    ('CA','Calculus & Optimization','Change, curvature and one-variable minima','#d28b3e'),
    ('PDSA','Python, DS & Algorithms','Trace code, complexity and graphs','#169a87'),
    ('DB','DBMS & Warehousing','SQL, normalization and analytics','#ca6674'),
    ('ML','Machine Learning','Models, evaluation and clustering','#2c87b7'),
    ('AI','Artificial Intelligence','Search, logic and uncertainty','#b17ac3'),
    ('GA','General Aptitude','Verbal, numerical, analytical and spatial','#83964b'),
]

rows=[]
for ln in (ROOT/'lessons.tsv').read_text(encoding='utf-8').splitlines():
    if not ln or ln.startswith('#'):continue
    parts=ln.split('|')
    assert len(parts)==8,(len(parts),ln[:65])
    sub,title,intuition,detail,formula,worked,shortcut,trap=parts
    lessonsub=sum(1 for x in rows if x['subject']==sub)+1
    rows.append(dict(id=f'{sub}-{lessonsub:03d}',subject=sub,title=title,meaning=intuition,explanation=detail,formula=formula,worked=worked,shortcut=shortcut,trap=trap))
assert len(rows)==158
questionrows=[]
for ln in (ROOT/'questions.tsv').read_text(encoding='utf-8').splitlines():
    if not ln or ln.startswith('#'):continue
    parts=ln.split('|')
    assert len(parts)==9,(len(parts),ln[:80])
    sub,qtype,marks,difficulty,prompt,opts,answer,explanation,tag=parts
    opts=opts.split('~') if opts else []
    assert qtype in ('MCQ','MSQ','NAT')
    if qtype!='NAT':assert len(opts)==4,(prompt,opts)
    if qtype=='MCQ':answer=int(answer);assert 0<=answer<4
    if qtype=='MSQ':answer=[int(x) for x in answer.split(',')];assert all(0<=x<4 for x in answer)
    if qtype=='NAT':answer=float(answer)
    id=f'Q{len(questionrows)+1:03d}'
    related=next((l['id'] for l in rows if l['subject']==sub and (tag.lower() in l['title'].lower() or l['title'].lower() in tag.lower())),None)
    if related is None:
        print('Unmatched tag',id,sub,tag)
        related=next(l['id'] for l in rows if l['subject']==sub)
    questionrows.append(dict(id=id,subject=sub,type=qtype,marks=int(marks),difficulty=difficulty,prompt=prompt,options=opts,answer=answer,solution=explanation,lesson_id=related))

by_sub=defaultdict(list)
for l in rows:by_sub[l['subject']].append(l)
# A staged beginner sequence keeps advanced ML/AI behind the mathematical and coding foundations.
phases=[
    {'PS':13,'LA':8,'PDSA':10,'CA':5,'GA':6},
    {'PS':13,'LA':9,'PDSA':11,'CA':5,'DB':4,'GA':4},
    {'PS':6,'DB':12,'ML':14,'AI':6,'GA':4},
    {'DB':5,'ML':11,'AI':9,'GA':3},
]
assert all(sum(p.get(s,0) for p in phases)==len(by_sub[s]) for s in by_sub), [(s,sum(p.get(s,0) for p in phases),len(by_sub[s])) for s in by_sub]

idx=defaultdict(int)
days=[]
start=date(2026,11,5)
qn=defaultdict(list)
for q in questionrows:qn[q['subject']].append(q)

for phase_num, p in enumerate(phases):
    # Spread each subject evenly over each 14-day block. Allow easy-first rotation.
    assigned=[[] for _ in range(14)]
    if phase_num==0:
        assigned[0]=['PS','PDSA','GA']
        for s in assigned[0]:p[s]-=1
    # Greedy balance: each concept goes to the lightest day, avoiding same subject twice/day.
    items=[]
    for s,n in p.items():
        for j in range(n):items.append(s)
    # weighted round-robin over subjects with count remaining, interleaved not block-by-block.
    r={s:n for s,n in p.items()}
    last=''
    while sum(r.values()):
        s=max((s for s in r if r[s]>0),key=lambda x: (r[x]/max(1,p[x]),r[x], x!=last))
        items_seen=sum(1 for a in assigned for _ in a)
        candidate=sorted(range(14),key=lambda d:(len(assigned[d]),s in assigned[d], (d-phase_num*2)%14))
        # Favor sparse days, avoid doubling on a day when possible.
        candidate=sorted(range(14),key=lambda d:(s in assigned[d],len(assigned[d]),(d-phase_num*2)%14))
        assigned[candidate[0]].append(s)
        r[s]-=1
        last=s
    for di,subs in enumerate(assigned):
        lesson_ids=[]
        for s in subs:
            lesson_ids.append(by_sub[s][idx[s]]['id']);idx[s]+=1
        day_number=len(days)+1
        d=start+timedelta(days=day_number-1)
        titles=[next(l['title'] for l in rows if l['id']==x) for x in lesson_ids]
        schedulefocus={'PS':'Probability intuition','LA':'Matrix thinking','PDSA':'Python & algorithms','CA':'Math foundations','DB':'Data systems','ML':'Learning machines','AI':'Reasoning systems','GA':'Aptitude edge'}
        dom=subs[0] if subs else 'GA'
        phase_name=['Build foundations','Strengthen core concepts','Learn applied DA','Complete the syllabus'][phase_num]
        day={'number':day_number,'date':d.isoformat(),'week':((day_number-1)//7)+1,'phase':phase_name,'kind':'learn','title':titles[0] if titles else phase_name,'focus':schedulefocus[dom],'lesson_ids':lesson_ids,'review_ids':[],'minutes':150 if d.weekday()<5 else 210}
        days.append(day)
assert len(days)==56
assert all(idx[k]==len(v) for k,v in by_sub.items()),idx
# 2 weeks: conceptual integration and structured revisiting of the full syllabus.
revision_pairs=[('PS','LA'),('PDSA','CA'),('DB','GA'),('ML','PS'),('AI','LA'),('PDSA','DB'),('ML','AI'),('PS','CA'),('GA','DB'),('PDSA','ML'),('AI','PS'),('LA','ML'),('DB','PDSA'),('PS','GA')]
for i,(a,b) in enumerate(revision_pairs):
    n=len(days)+1;d=start+timedelta(days=n-1)
    aa=by_sub[a]; bb=by_sub[b]
    # Distribute review samples to touch early, middle and late lessons.
    rev=[]
    for x,offset in ((aa,i*3),(bb,i*4)):
        rev += [x[(offset+j)%len(x)]['id'] for j in range(min(3,len(x)))]
    days.append({'number':n,'date':d.isoformat(),'week':((n-1)//7)+1,'phase':'Integrate & revisit','kind':'review','title':f'{next(x[1] for x in SUBJECTS if x[0]==a)} + {next(x[1] for x in SUBJECTS if x[0]==b)}','focus':'Mixed revision and error correction','lesson_ids':[],'review_ids':rev,'minutes':180 if d.weekday()<5 else 240})
assert len(days)==70
for i in range(14):
    n=len(days)+1; d=start+timedelta(days=n-1)
    mock=i in (0,3,6,9,12)
    a,b=revision_pairs[(i*5+3)%len(revision_pairs)]
    rev=[x['id'] for x in by_sub[a][::max(1,len(by_sub[a])//4)][:4]]+[x['id'] for x in by_sub[b][::max(1,len(by_sub[b])//4)][:4]]
    days.append({'number':n,'date':d.isoformat(),'week':((n-1)//7)+1,'phase':'GATE simulation & repair','kind':'mock' if mock else 'review','title':f'Full GATE-format mock {sum(z["kind"]=="mock" for z in days)+1}' if mock else f'Error clinic: {next(x[1] for x in SUBJECTS if x[0]==a)} + {next(x[1] for x in SUBJECTS if x[0]==b)}','focus':'Timed practice and revision','lesson_ids':[],'review_ids':rev,'minutes':210 if mock else 180})
assert len(days)==84
finals=[('Final full-length practice','mock'),('Formula maps and high-yield identities','review'),('Weakest-topic rescue','review'),('Reasoning, definitions and exam strategy','review'),('Light recall and readiness check','review')]
for title,kind in finals:
    n=len(days)+1;d=start+timedelta(days=n-1)
    rev=[by_sub[s][(n*7)%len(by_sub[s])]['id'] for s in ['PS','LA','CA','PDSA','DB','ML','AI','GA']]
    days.append({'number':n,'date':d.isoformat(),'week':((n-1)//7)+1,'phase':'Final five-day taper','kind':kind,'title':title,'focus':'Calm, targeted finishing work','lesson_ids':[],'review_ids':rev,'minutes':190 if kind=='mock' else 120})
assert len(days)==89 and days[-1]['date']=='2027-02-01'

# Repeatable daily quizzes: prefer exactly mapped lesson questions plus broad subject drilling;
# never claim the resulting mixed question sets are real previous-year papers.
for day in days:
    rng=random.Random(2027+day['number']*83)
    if day['kind']=='mock':
        by=defaultdict(list)
        for q in questionrows:by[q['subject']].append(q['id'])
        # Exact 100-mark GATE-style count: 30 one-mark + 35 two-mark questions.
        # 10 GA questions yield exactly 15 marks; 55 DA questions yield 85 marks.
        spec={'GA':10,'PS':11,'LA':7,'CA':4,'PDSA':10,'DB':8,'ML':9,'AI':6}
        one={'GA':5,'PS':6,'LA':3,'CA':2,'PDSA':4,'DB':4,'ML':3,'AI':3}
        qids=[]
        for s,n in spec.items():
            one_q=[q['id'] for q in questionrows if q['subject']==s and q['marks']==1]
            two_q=[q['id'] for q in questionrows if q['subject']==s and q['marks']==2]
            qids+=rng.sample(one_q,one[s])+rng.sample(two_q,n-one[s])
        assert len(qids)==65 and sum(next(q['marks'] for q in questionrows if q['id']==id) for id in qids)==100
        rng.shuffle(qids)
    else:
        selected=day['lesson_ids'] or day['review_ids']
        ss=list(dict.fromkeys(next(l['subject'] for l in rows if l['id']==lid) for lid in selected))
        related=[q['id'] for q in questionrows if q['lesson_id'] in selected]
        rng.shuffle(related)
        qids=related[:6]
        if day['kind']=='learn':
            target=8
        else:target=15
        pools=[q['id'] for q in questionrows if q['subject'] in ss and q['id'] not in qids]
        if len(pools)<target-len(qids):pools=[q['id'] for q in questionrows if q['id'] not in qids]
        qids+=rng.sample(pools,min(target-len(qids),len(pools)))
        # put one GA question on ordinary learning days for a micro dose of aptitude
        if 'GA' not in ss and day['kind']=='learn':
            ga=rng.choice(qn['GA'])['id'];qids[-1]=ga
        rng.shuffle(qids)
    day['question_ids']=qids

metadata=dict(name='GATE DA 2027 · StudyOS',start=start.isoformat(),end=days[-1]['date'],exam_note='The official GATE 2027 exam dates start February 6; this study plan ends February 1.',total_days=89,source_da='https://gate2027.iitm.ac.in/static/doc/GATE2027_Syllabus/DA_GATE2027_Syllabus.pdf',source_ga='https://gate2027.iitm.ac.in/static/doc/GATE2027_Syllabus/GA_GATE2027_Syllabus.pdf',source_pattern='https://gate2027.iitm.ac.in/question_paper_pattern')
# Keep the expanded, hand-authored explanation pack whenever the content is rebuilt.
rich={}
for raw in (ROOT/'enrichment.tsv').read_text(encoding='utf-8').splitlines():
    if not raw or raw.startswith('#'):continue
    parts=raw.split('|')
    assert len(parts)==6,(raw[:60],len(parts))
    id,intuition,reasoning,steps,check,answer=parts
    assert id not in rich
    rich[id]=dict(intuition=intuition,reasoning=reasoning,solved_steps=steps.split('~~'),check_question=check,check_answer=answer)
assert set(rich)=={x['id'] for x in rows}
for x in rows:x['deep']=rich[x['id']]
metadata['edition']='Detailed Lessons 2.0'
metadata['lesson_format']='Foundation + clear reasoning + formula + two worked examples + concept check + exam traps'
out={'meta':metadata,'subjects':[{'id':s,'name':n,'subtitle':z,'color':c} for s,n,z,c in SUBJECTS],'lessons':rows,'days':days,'questions':questionrows}
(ROOT/'content.json').write_text(json.dumps(out,ensure_ascii=False,indent=1),encoding='utf-8')
print(f'{len(rows)} lessons, {len(questionrows)} original questions, {len(days)} days, {(ROOT/"content.json").stat().st_size/1024:.1f} KiB content pack')
print('Quiz',Counter(d['kind'] for d in days),'coverage',Counter(l['subject'] for l in rows))

# Regenerate the independent deep-course layer after updating the base curriculum.
import compile_deep_course
compile_deep_course.main()
