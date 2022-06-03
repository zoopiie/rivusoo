import win32gui
import pyautogui


pyautogui.FAILSAFE = False

while True:
    win32gui.GetCursorPos()
    x, y = win32gui.GetCursorPos()
    if x < 75 and y > 980:
        pyautogui.moveTo(890, 250, 2, pyautogui.easeOutQuad)
        pyautogui.doubleClick()