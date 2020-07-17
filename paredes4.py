from pynput.keyboard import Listener
from pynput.mouse import Button,Listener
from pynput import *

import pyautogui
import pyautogui as pg
import pyautogui as pa
import sys
import os

klik = "p"


def capt(key):
    tecla = str(key)
    print("tecla")
    tecla = tecla.replace("'", "")
    if tecla == "q":
        def funtionclick(x,y,button,pressed):
            click=button
            print(click)
            klik=click

            if klik =="button.right":
                pyautogui.hotkey("ctrl")
                pa.moveTo(1810,100)
                pg.click(1810,100)
                pyautogui.hotkey("ctrl")

            elif klik =="button.left":
                pyautogui.hotkey("ctrl")
                pa.moveTo(1810,100)
                pg.click(1810,100)
                pyautogui.hotkey("ctrl")

            elif tecla == 2:
                pyautogui.hotkey("ctrl")
                pa.moveTo(1810,100)
                pg.click(1810,100)
                pyautogui.hotkey("ctrl")
        with Listener(on_click=funtionclick) as listener:
                listener.join()



    if tecla == "g":
        print("perro")
    if tecla == "p":
        sys.exit()




with Listener(on_press=capt) as c:
    c.join()
