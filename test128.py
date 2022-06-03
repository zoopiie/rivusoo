import pyautogui
from time import sleep
from datetime import datetime

pyautogui.FAILSAFE = False

pyautogui.moveTo(100, 100, 1, pyautogui.easeOutQuad)
now = datetime.now()

dt_string = now.strftime("%H:%M:%S")
print(dt_string)
pyautogui.moveTo(1850, 100, 15, pyautogui.easeOutQuad)
pyautogui.moveTo(1850, 950, 15, pyautogui.easeOutQuad)
pyautogui.moveTo(100, 950, 15, pyautogui.easeOutQuad)
pyautogui.moveTo(100, 100, 15, pyautogui.easeOutQuad)
now = datetime.now()

dt_string = now.strftime("%H:%M:%S")
print(dt_string)