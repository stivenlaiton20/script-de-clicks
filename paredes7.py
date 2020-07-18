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
    if click == Button.left:
        print("click izquierdo")
        pa.moveTo(1810,100)


    elif click == Button.right:
        print("click derecho")
        pa.moveTo(1810,100)

    else:
        print("click cualquiera")


with Listener(on_click=funtionclick) as listener:
    listener.join()
