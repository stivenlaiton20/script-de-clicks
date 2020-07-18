from pynput.keyboard import Listener
from pynput.mouse import Button,Listener
from pynput import *

import pyautogui
import pyautogui as pg
import pyautogui as pa
import sys
import os



def capt(key):
    tecla = str(key)
    print("tecla")
    tecla = tecla.replace("'", "")
    if tecla == "q":
        print("espichaste")
        pa.moveTo(1810,100)
    elif tecla == "g":
        print("perro")
    elif tecla == "p":
        sys.exit()
    else:
        print("tecla incorrecta")
with Listener(on_press=capt) as c:
    c.join()
