from pynput.keyboard import Listener
from pynput import *
import pyautogui
import pyautogui as pg
import pyautogui as pa
import sys
import os
from io import open

def capt(key):
    tecla = str(key)
    print(tecla)
    tecla = tecla.replace("'", "")
    if tecla == 'q':
        import paredes7
        paredes7.funtionclick()

    elif tecla == "g":
        print("perro")
    elif tecla == "p":
        sys.exit()


with Listener(on_press=capt) as c:
    c.join()
