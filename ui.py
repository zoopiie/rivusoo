from time import sleep
import pyautogui
import keyboard

while True :
    if keyboard.is_pressed("F1"):
        for i in range(150):
            pyautogui.click(button='left')
