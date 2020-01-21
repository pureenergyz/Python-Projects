import urllib.request
import time
import pyautogui
import webbrowser
url = 'https://' # Enter URL here.
webbrowser.open_new(url) # Command opens web browser.
time.sleep(10) # Command pauses code.
pyautogui.moveTo(561, 164, duration = 1) # Command moves the mouse.
pyautogui.click(clicks=1) # Command left clicks 1 time.
pyautogui.write('username') # Enter username supplied by administrator.
pyautogui.moveTo(564, 210, duration = 1)
pyautogui.click(clicks=1) # Command left clicks 1 time. 
pyautogui.write('password') # Enter username supplied by administrator.
pyautogui.press('enter') # Command presses enter on keyboard. 
time.sleep(20) # Command pauses code.
myScreenshot = pyautogui.screenshot() # Command takes a screen shot.
myScreenshot.save(r'File Path') # Enter file destination here.
pyautogui.moveTo(118, 718, duration = 1)
pyautogui.click(clicks=2) # Command left clicks 2 times.
myScreenshot = pyautogui.screenshot() # Command takes a screen shot.
myScreenshot.save(r'File Path') # Enter file destination here.

