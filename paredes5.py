from pynput.keyboard import Listener
from pynput.mouse import Button,Listener
from pynput import *

import pyautogui
import pyautogui as pg
import pyautogui as pa
import sys
import os
clickrojo=pg.click()
def funtionclick(x,y,button,pressed):
    click=button
    print(click)
    while (1):
        if click == Button.left:
            print("click izquierdo")
            pyautogui.hotkey("ctrl")
            pa.moveTo(1810,100)
            pyautogui.hotkey("ctrl")
            break

        elif click == Button.right:
            print("click derecho")
            pyautogui.hotkey("ctrl")
            pa.moveTo(1810,100)
            pyautogui.hotkey("ctrl")
            break

        else:
            print("click cualquiera")
            break


with Listener(on_click=funtionclick) as listener:
    listener.join()
