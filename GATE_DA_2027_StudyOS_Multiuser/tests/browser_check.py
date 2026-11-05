"""Optional Playwright smoke test for auth screens and study pages."""
import os, subprocess, sys, tempfile, time, socket
from pathlib import Path
from urllib.request import urlopen
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
db=tempfile.TemporaryDirectory()
sock=socket.socket();sock.bind(('127.0.0.1',0));port=sock.getsockname()[1];sock.close()
proc=subprocess.Popen([sys.executable,'server.py','--port',str(port)],cwd=root,env={**os.environ,'STUDYOS_DATA_DIR':db.name},stdout=subprocess.DEVNULL)
base='http://127.0.0.1:'+str(port)
for i in range(80):
 try:
  urlopen(base+'/api/health',timeout=1);break
 except Exception:time.sleep(.1)
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  page=browser.new_page(viewport={'width':1360,'height':900},device_scale_factor=1)
  errors=[]
  page.on('pageerror',lambda e: errors.append(str(e)))
  page.goto(base,wait_until='domcontentloaded')
  page.locator('#auth-screen').wait_for(state='visible')
  page.screenshot(path=str(root/'preview_login.png'),full_page=True)
  page.click('#auth-mode-register')
  page.locator('#auth-display').fill('Example Learner')
  page.locator('#auth-username').fill('example_student')
  page.locator('#auth-password').fill('myVeryStrongPass123')
  page.click('#auth-submit')
  page.locator('#sidebar').wait_for(state='visible',timeout=10000)
  page.locator('#account-display').wait_for(state='visible')
  assert 'Example Learner' in page.locator('#account-display').inner_text()
  page.screenshot(path=str(root/'preview_dashboard_logged_in.png'),full_page=True)
  page.click('[data-view="settings"]')
  page.get_by_text('Change password').wait_for(state='visible')
  page.click('#logout-button')
  page.locator('#auth-screen').wait_for(state='visible')
  # Re-login same account, ensure dashboard opens.
  page.locator('#auth-username').fill('example_student')
  page.locator('#auth-password').fill('myVeryStrongPass123')
  page.click('#auth-submit')
  page.locator('#account-display').wait_for(state='visible')
  assert not errors,errors
  print('Desktop login, registration, settings and logout: PASS')
  mobile=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1)
  mobile.goto(base,wait_until='domcontentloaded')
  mobile.locator('#auth-screen').wait_for(state='visible')
  mobile.screenshot(path=str(root/'preview_mobile_login.png'),full_page=True)
  print('Mobile auth layout: PASS')
  browser.close()
finally:
 proc.terminate();proc.wait(timeout=5);db.cleanup()
