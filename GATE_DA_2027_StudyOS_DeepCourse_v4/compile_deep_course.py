"""Build the v4 guided-course content pack without changing any user progress data.

Use `python compile_deep_course.py` after editing topic_challenges.tsv or
foundations/*.md. If `build_data.py` is run first, rerun this script.
"""
from __future__ import annotations
import json, re
from pathlib import Path
from collections import defaultdict
ROOT=Path(__file__).resolve().parent
CONTENT=ROOT/'content.json'
SUBS=['PS','LA','CA','PDSA','DB','ML','AI','GA']
# Map each of the 158 concepts to a genuinely relevant part of its foundation handbook.
SECTION_MAP={
'PS': [(1,6,0),(7,10,2),(11,16,3),(17,26,4),(27,32,5)],
'LA': [(1,1,0),(2,4,1),(5,9,2),(10,11,3),(12,14,4),(15,17,5)],
'CA': [(1,1,0),(2,3,0),(4,4,1),(5,5,2),(6,6,4),(7,9,3),(10,10,5)],
'PDSA': [(1,1,0),(2,3,1),(4,5,2),(6,7,3),(8,13,4),(14,17,4),(18,21,5)],
'DB': [(1,2,0),(3,5,1),(6,9,2),(10,11,4),(12,13,5),(14,14,6),(15,18,8),(19,21,7)],
'ML': [(1,1,0),(2,2,1),(3,5,1),(6,6,2),(7,8,3),(9,13,4),(14,15,5),(16,18,6),(19,23,7),(24,25,7)],
'AI': [(1,1,0),(2,3,1),(4,5,2),(6,7,3),(8,11,4),(12,15,6)],
'GA': [(1,5,1),(6,7,2),(8,10,3),(11,13,4),(14,15,5),(16,17,6)]
}

def parse_foundation(path:Path):
    raw=path.read_text(encoding='utf-8').strip()
    lines=raw.splitlines()
    assert lines[0].startswith('# '),path
    course={'subject':path.stem,'title':lines[0][2:].strip(),'sections':[]}
    for block in re.split(r'(?m)^## ',raw)[1:]:
        title,_,body=block.partition('\n')
        paragraphs=[p.replace('\n',' ').strip() for p in re.split(r'\n\s*\n',body.strip()) if p.strip()]
        assert paragraphs,path
        course['sections'].append({'title':title.strip(),'paragraphs':paragraphs})
    course['words']=len(raw.split())
    return course

def main():
    j=json.loads(CONTENT.read_text(encoding='utf-8'))
    challenges={}
    for line in (ROOT/'topic_challenges.tsv').read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'):continue
        parts=line.split('|',3)
        if len(parts)!=4:raise ValueError(f'Bad challenge line {line[:80]}')
        lid,context,problem,solution=parts
        if lid in challenges:raise ValueError(f'Duplicate {lid}')
        challenges[lid]={'context':context,'problem':problem,'solution':solution}
    concepts={x['id'] for x in j['lessons']}
    assert set(challenges)==concepts,(set(challenges)-concepts,concepts-set(challenges))
    foundations={s:parse_foundation(ROOT/'foundations'/f'{s}.md') for s in SUBS}
    for l in j['lessons']:
        l['applied']=challenges[l['id']]
        n=int(l['id'].split('-')[1]); sub=l['subject']
        candidates=[i for lo,hi,i in SECTION_MAP[sub] if lo<=n<=hi]
        assert candidates,(l['id'],sub,n)
        i=candidates[0]
        assert i<len(foundations[sub]['sections']),l['id']
        l['foundation_section']=i
    j['foundations']=foundations
    j['meta']['edition']='Deep Course v4 — 158 concept challenges + 8 foundation handbooks'
    j['meta']['lesson_format']='First principles, derivations, foundation reading, two original solved examples, one new applied challenge with reveal, graded exam practice'
    j['meta']['applied_challenges']=len(challenges)
    j['meta']['foundation_words']=sum(x['words'] for x in foundations.values())
    CONTENT.write_text(json.dumps(j,ensure_ascii=False,indent=1),encoding='utf-8')
    # Create an offline readable companion: all eight handbooks and all 158 tailored extra challenges.
    bysub=defaultdict(list)
    for l in j['lessons']:bysub[l['subject']].append(l)
    guide=['# GATE DA StudyOS — Deep Course v4',
           'Self-contained eight-subject foundation handbooks plus extra applied learning problems for all 158 concepts.',
           'This supplements, rather than replaces, the detailed lesson workbook and original scored practice bank.',
           '']
    for sub in SUBS:
        guide.append((ROOT/'foundations'/f'{sub}.md').read_text(encoding='utf-8').strip())
        guide.append('\n## Extended applied problems for this subject\n')
        for l in bysub[sub]:
            a=l['applied'];guide.extend([f'### {l["id"]}: {l["title"]}',f'**Core connection:** {a["context"]}',f'**Try independently:** {a["problem"]}',f'**Worked answer:** {a["solution"]}',''])
        guide.append('\n---\n')
    (ROOT/'DEEP_COURSE_HANDBOOK.md').write_text('\n\n'.join(guide),encoding='utf-8')
    print('Subjects',len(foundations),'sections',sum(len(x['sections']) for x in foundations.values()),'foundation words',sum(x['words'] for x in foundations.values()))
    print('Lessons with new challenges:',len(challenges),'content size KiB:',round(CONTENT.stat().st_size/1024),'offline handbook words:',len(' '.join(guide).split()))

if __name__=='__main__':main()
