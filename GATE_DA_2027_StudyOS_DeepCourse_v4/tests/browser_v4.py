"""Optional v4 smoke test; requires Playwright and Chrome."""
import os,subprocess,sys,tempfile,time,socket
from pathlib import Path
from urllib.request import urlopen
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as tmp:
    sock=socket.socket();sock.bind(('127.0.0.1',0));port=sock.getsockname()[1];sock.close()
    proc=subprocess.Popen([sys.executable,'server.py','--port',str(port)],cwd=root,env={**os.environ,'STUDYOS_DATA_DIR':tmp},stdout=subprocess.DEVNULL)
    base=f'http://127.0.0.1:{port}'
    for _ in range(50):
        try:urlopen(base+'/api/health',timeout=1);break
        except Exception:time.sleep(.1)
    try:
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
            page=browser.new_page(viewport={'width':1450,'height':950})
            errors=[];page.on('pageerror',lambda e: errors.append(str(e)))
            page.goto(base)
            page.locator('#auth-screen').wait_for(state='visible')
            page.locator('#auth-mode-register').click()
            page.locator('#auth-display').fill('Test Learner')
            page.locator('#auth-username').fill('test_deep_course')
            page.locator('#auth-password').fill('TestLearnerPassphrase123')
            page.locator('#auth-submit').click()
            page.locator('#account-display').wait_for(state='visible')
            page.locator('[data-view="foundations"]').click()
            page.get_by_text('Read before memorizing').wait_for(state='visible')
            page.locator('button[data-foundation="PS"]').first.click()
            page.get_by_text('1. Start with uncertainty, not formulas').first.wait_for(state='visible')
            page.screenshot(path=str(root/'preview_foundations_v4.png'),full_page=False)
            page.locator('button[data-subject="PS"]').last.click()
            page.locator('button[data-lesson="PS-001"]').first.click()
            page.get_by_text('Sets and sample spaces',exact=True).wait_for(state='visible')
            page.get_by_text('Can you transfer the idea to a new situation?').wait_for(state='visible')
            answer=page.locator('.applied-answer')
            assert answer.is_hidden()
            page.locator('button[data-reveal-applied]').click()
            assert answer.is_visible()
            assert '2×2×6=24' in answer.inner_text()
            page.screenshot(path=str(root/'preview_concept_v4.png'),full_page=False)
            page.locator('button[data-topic-toggle="PS-001"]').last.click()
            page.wait_for_timeout(200)
            page.reload()
            page.locator('button[data-view="syllabus"]').click()
            page.locator('button[data-subject="PS"]').first.click()
            page.locator('button[data-topic-toggle="PS-001"]').first.wait_for()
            assert 'checked' in page.locator('button[data-topic-toggle="PS-001"]').first.get_attribute('class')
            assert not errors,errors
            mobile=browser.new_page(viewport={'width':390,'height':844})
            mobile.goto(base)
            mobile.locator('#auth-screen').wait_for(state='visible')
            print('Browser v4 desktop courses, applied challenge reveal, persisted completion, mobile login: PASS')
            browser.close()
    finally:proc.terminate();proc.wait(timeout=5)
