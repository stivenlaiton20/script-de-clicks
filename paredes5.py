
from pynput.keyboard import Listener
from pynput.mouse import Button,Listener
from pynput import *

import pyautogui
import pyautogui as pg
import pyautogui as pa
import sys
import os
def funtionclick(x,y,button,pressed):
    click=button
    if click =="button.right":
        print("click izquierdo")
        pyautogui.hotkey("ctrl")
        pa.moveTo(1810,100)
        pg.click(1810,100)
        pyautogui.hotkey("ctrl")

    else:
        click =="button.left":
        pyautogui.hotkey("ctrl")
        print("click izquierdo")
        pa.moveTo(1810,100)
        pg.click(1810,100)
        pyautogui.hotkey("ctrl")



with Listener(on_click=funtionclick) as listener:
    listener.join()
