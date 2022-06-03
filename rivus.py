from tkinter import *
import random
from time import sleep
import pyautogui
import os
import keyboard
import win32gui


pyautogui.FAILSAFE = False
m = 3
i = 0

def alt():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('f4')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('f4')
    pyautogui.press('enter')
    pyautogui.moveTo(890, 250, 2, pyautogui.easeOutQuad)
    pyautogui.doubleClick()


def ctrl():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('w')
    pyautogui.keyUp('w')
    pyautogui.keyUp('ctrl')




def dep():
    sleep(0.2)
    pyautogui.doubleClick()
    c = random.randint(12,1024)
    d = random.randint(12, 1024)
    pyautogui.moveTo(c, d, 2, pyautogui.easeOutQuad)
    pyautogui.click(button='right')
    c = random.randint(12, 1024)
    d = random.randint(12, 1024)
    pyautogui.moveTo(c, d, 2, pyautogui.easeOutQuad)
    pyautogui.click(button='middle')



def truc():
    os.popen('python test.py')
    os.system('start cmd')

    pyautogui.moveTo(54, 986, 2, pyautogui.easeOutQuad)
    pyautogui.write('setvol.exe', interval=0.001)
    pyautogui.press('enter')
    sleep(0.1)
    pyautogui.write('setvol unmute', interval=0.001)
    pyautogui.press('enter')
    sleep(0.1)
    pyautogui.write('setvol 60', interval=0.001)
    pyautogui.press('enter')
    pyautogui.moveTo(364, 124, 2, pyautogui.easeOutQuad)
    pyautogui.write('hostname', interval=0.001)
    pyautogui.press('enter')
    pyautogui.moveTo(364, 124, 2, pyautogui.easeOutQuad)

    pyautogui.write('ipconfig /all', interval=0.001)
    pyautogui.press('enter')
    pyautogui.moveTo(124, 684, 2, pyautogui.easeOutQuad)

    pyautogui.write('netstat -a -n', interval=0.001)
    pyautogui.press('enter')
    pyautogui.moveTo(890, 706, 2, pyautogui.easeOutQuad)
    pyautogui.write('hacking....', interval=0.001)

    sleep(1)

    os.popen('FUN.mp4')
    pyautogui.moveTo(100, 100, 3, pyautogui.easeOutQuad)
    pyautogui.moveTo(1850, 100, 15, pyautogui.easeOutQuad)
    pyautogui.moveTo(1850, 950, 15, pyautogui.easeOutQuad)
    pyautogui.moveTo(100, 950, 15, pyautogui.easeOutQuad)
    pyautogui.moveTo(100, 100, 15, pyautogui.easeOutQuad)



    for i in range (10):
        a = random.randint(0,3)
        if (a==0):
            for i in range (10):
                os.popen('python rivus2.py')
                sleep(0.2)
        if (a == 1):
            os.popen('python rivus3.py')
        if (a==2):
            os.popen('python rivus4.py')
        dep()


truc()

while True:
    win32gui.GetCursorPos()
    x, y = win32gui.GetCursorPos()
    if x < 75 and y > 980:
        pyautogui.moveTo(890, 250, 2, pyautogui.easeOutQuad)
        pyautogui.doubleClick()

    if keyboard.is_pressed("space"):
        ctrl()
    if keyboard.is_pressed("enter"):
        alt()