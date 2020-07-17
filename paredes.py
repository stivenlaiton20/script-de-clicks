from pynput.mouse import Button,Listener


def funtionclick(x,y,button,pressed):
    print(button)




with Listener(on_click=funtionclick) as listener:
    listener.join()
