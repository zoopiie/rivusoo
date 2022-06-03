import os
import pyautogui
from time import sleep



os.system('start cmd')
pyautogui.moveTo(54, 986, 2, pyautogui.easeOutQuad)
sleep(0.1)
pyautogui.write('FUN.mp4', interval=0.001)
pyautogui.press('enter')
sleep(0.1)
pyautogui.write('setvol unmute', interval=0.001)
pyautogui.press('enter')
sleep(0.1)
pyautogui.write('setvol 60', interval=0.001)
pyautogui.press('enter')