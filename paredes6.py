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
    print(click)
    if click == Button.left:
        print("click izquierdo")
    elif click == Button.right:
        print("click derecho")
    else:
        print("click cualquiera")


with Listener(on_click=funtionclick) as listener:
    listener.join()
