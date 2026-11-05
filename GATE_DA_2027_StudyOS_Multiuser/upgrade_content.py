"""Attach 158 additional, topic-authored beginner explanations to the existing site.
Run after editing enrichment.tsv; does not touch any SQLite user progress.
"""
from pathlib import Path
from collections import Counter
import json

ROOT=Path(__file__).resolve().parent
pack=json.loads((ROOT/'content.json').read_text(encoding='utf-8'))
rich={}
for raw in (ROOT/'enrichment.tsv').read_text(encoding='utf-8').splitlines():
    if not raw or raw.startswith('#'):continue
    parts=raw.split('|')
    assert len(parts)==6, (raw[:90],len(parts))
    id,intuition,mechanism,example,check,answer=parts
    assert id not in rich
    rich[id]={'intuition':intuition,'reasoning':mechanism,'solved_steps':example.split('~~'),'check_question':check,'check_answer':answer}
valid={l['id'] for l in pack['lessons']}
assert set(rich)==valid,('missing',sorted(valid-set(rich)),'extra',sorted(set(rich)-valid))
for lesson in pack['lessons']:lesson['deep']=rich[lesson['id']]
pack['meta']['edition']='Detailed Lessons 2.0'
pack['meta']['lesson_format']='Foundation + clear reasoning + formula + two worked examples + concept check + exam traps'
(ROOT/'content.json').write_text(json.dumps(pack,ensure_ascii=False,indent=1),encoding='utf-8')
questions={q['lesson_id']:q for q in pack['questions']}
subs={s['id']:s['name'] for s in pack['subjects']}
lines=['# GATE DA 2027 — Expanded Beginner Study Guide',
       '', 'All 158 syllabus concepts with intuition, reasoning, formulas, two worked examples, misconception checks, original exam-style practice and answer explanations. This is a supplementary revision and learning guide, not an authorized reproduction of previous-year papers.',
       '', 'Recommended learning loop: read the mental model → understand why the formula works → cover the solved steps and solve on paper → attempt the prediction check → complete the related quiz in the website. Your answers to the website quiz are scored and saved in the SQLite backend.', '',
       'The lessons deliberately teach principles and worked methods; a full textbook or an exhaustive archive of GATE past papers will still provide additional depth and variety.','']
last=None
for l in pack['lessons']:
    if l['subject']!=last:
        lines.extend(['',f"# {subs[l['subject']]}",''])
        last=l['subject']
    d=l['deep']
    lines.extend(['',f"## {l['id']} — {l['title']}",'',
                  '### Learning goal',l['meaning'],'',
                  '### Intuition — what the idea means',d['intuition'],'',
                  '### How and why the method works',l['explanation'],'',d['reasoning'],'',
                  '### Key formula or property',f"`{l['formula']}`",'',
                  '### First solved example',l['worked'],'',
                  '### Second solved example — step by step',''])
    for i,step in enumerate(d['solved_steps']):
        lines.append((f"{i}. " if i else '')+step if i==0 else f"{i}. {step}")
    lines.extend(['','### Try before revealing the answer',f"**Question:** {d['check_question']}", '',
                  '<details><summary>Show explanation</summary>',d['check_answer'],'</details>','',
                  '### GATE examination technique',f"- **Shortcut:** {l['shortcut']}",f"- **Common trap:** {l['trap']}",''])
    q=questions.get(l['id'])
    if q:
        lines.extend(['### Original GATE-style question',f"**{q['type']} · {q['marks']} mark(s):** {q['prompt']}",''])
        if q['options']:
            lines.extend([f"- {chr(65+i)}. {op}" for i,op in enumerate(q['options'])]);lines.append('')
        ans=q['answer']
        if isinstance(ans,list):ans=', '.join(chr(65+x) for x in ans)
        elif q['type']=='MCQ':ans=chr(65+ans)
        lines.extend(['<details><summary>Show correct answer</summary>',f"**Answer:** {ans}",q['solution'],'</details>',''])
    lines.extend(['---',''])
(ROOT/'DETAILED_STUDY_GUIDE_158_CONCEPTS.md').write_text('\n'.join(lines),encoding='utf-8')
print('Updated detailed content:',len(rich),'lessons,',sum(len(x.split()) for x in lines),'guide words,',Counter(x['subject'] for x in pack['lessons']))
