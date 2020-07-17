
from pynput.keyboard import Listener
from pynput import *

import pyautogui
import pyautogui as pg
import pyautogui as pa
import sys
import os
def eventoclik(click):
    verd= click == pyautogui.click(button='left')
    return verd

def capt(key):
    tecla = str(key)
    tecla = tecla.replace("'", "")
    if tecla == 'q':
        while (1):
            if eventoclik():
                pyautogui.hotkey("ctrl")
                pa.moveTo(1810,100)
                pg.click(1810,100)
                pyautogui.hotkey("ctrl")
                break
            elif pyautogui.click(button='right'):
                pyautogui.hotkey("ctrl")
                pa.moveTo(1810,100)
                pg.click(1810,100)
                pyautogui.hotkey("ctrl")
                break
            elif tecla == 2:
                pyautogui.hotkey("ctrl")
                pa.moveTo(1810,100)
                pg.click(1810,100)
                pyautogui.hotkey("ctrl")
                break


    if tecla == 'Key.escape':
        print("perro")
    if tecla == "p":
        sys.exit()

with Listener(on_press=capt) as c:
    c.join()
