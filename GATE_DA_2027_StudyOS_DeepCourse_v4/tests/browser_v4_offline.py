"""Smoke-test v4 UI offline when localhost is blocked by browser policy.
Uses real app.js and rendered HTML with mocked fetch; does not test the backend.
"""
import json,re
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
html=(root/'static/index.html').read_text()
html=re.sub(r'<link rel="stylesheet" href="/static/style.css"\s*/>', '',html)
html=re.sub(r'<script src="/static/app.js" defer></script>', '',html)
content=json.loads((root/'content.json').read_text())
progress={"topics":{},"day_tasks":{},"notes":{},"recalls":{},"recent_attempts":[],"settings":{"daily_minutes":"150"},"active_days":[],"quiz_count_by_day":{},"subject_accuracy":{},"streak":0}
# Authenticated course bootstrap returns safe public questions without correct answers.
for q in content['questions']:
 q.pop('answer',None);q.pop('solution',None)
bootstrap={"content":content,"progress":progress,"server_date":"2026-11-05"}
payload=json.dumps(bootstrap,ensure_ascii=False)
mock='''window.fetch=async (url,opts={})=>{
const path=String(url);let data={},status=200;
if(path==='/api/me')data={authenticated:true,user:{username:'smoke',display_name:'Smoke Test'},csrf_token:'test-csrf',registration_enabled:true};
else if(path==='/api/bootstrap')data=window.__data;
else if(path==='/api/topic'){const b=JSON.parse(opts.body);window.__data.progress.topics[b.id]=b.completed;data={ok:true,completed:b.completed};}
else if(path==='/api/note'){const b=JSON.parse(opts.body);window.__data.progress.notes[b.id]=b.text;data={ok:true};}
else if(path==='/api/day'){const b=JSON.parse(opts.body);window.__data.progress.day_tasks[b.day]??={};window.__data.progress.day_tasks[b.day][b.task]=b.completed;data={ok:true};}
else data={ok:true};
return {ok:status<400,status,json:async()=>data};
};'''
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.set_content(html,wait_until='domcontentloaded')
 page.add_style_tag(content=(root/'static/style.css').read_text())
 page.evaluate('window.__data='+payload+';')
 page.add_script_tag(content=mock)
 page.add_script_tag(content=(root/'static/app.js').read_text())
 page.locator('#app').wait_for(state='visible')
 page.locator('button[data-view="foundations"]').click()
 page.get_by_text('Read before memorizing').wait_for(state='visible')
 page.screenshot(path=str(root/'preview_foundation_courses_v4.png'))
 page.locator('button[data-foundation="PS"]').first.click()
 page.get_by_text('1. Start with uncertainty, not formulas').first.wait_for(state='visible')
 page.screenshot(path=str(root/'preview_foundation_chapter_v4.png'))
 page.locator('button[data-subject="PS"]').last.click()
 page.locator('button[data-lesson="PS-001"]').first.click()
 page.get_by_text('Can you transfer the idea to a new situation?').wait_for(state='visible')
 answer=page.locator('.applied-answer')
 assert answer.is_hidden()
 page.locator('button[data-reveal-applied]').click()
 assert answer.is_visible()
 assert '2×2×6=24' in answer.inner_text()
 page.screenshot(path=str(root/'preview_expanded_lesson_v4.png'),full_page=True)
 page.locator('button[data-topic-toggle="PS-001"]').last.click()
 assert page.locator('button[data-topic-toggle="PS-001"]').last.inner_text().startswith('✓')
 assert not errors,errors
 print('Offline browser UI: 8 course cards, foundation chapter, revealed applied solution, mark mastered PASS')
 mobile=browser.new_page(viewport={'width':390,'height':844})
 mobile.set_content(html,wait_until='domcontentloaded')
 mobile.add_style_tag(content=(root/'static/style.css').read_text())
 mobile.evaluate('window.__data='+payload+';')
 mobile.add_script_tag(content=mock)
 mobile.add_script_tag(content=(root/'static/app.js').read_text())
 mobile.locator('#app').wait_for(state='visible')
 mobile.locator('#menu-toggle').click()
 mobile.locator('[data-view="foundations"]').click()
 mobile.locator('button[data-foundation="PS"]').first.click()
 mobile.screenshot(path=str(root/'preview_mobile_v4.png'))
 print('Offline mobile UI: navigation and foundation reading PASS')
 browser.close()
