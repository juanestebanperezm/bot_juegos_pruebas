import os
import pyautogui as pg 
import time

def multiple(): 

    time.sleep(3)

    lib = [i for i in os.listdir() if i.endswith(".png")]
    while True:
        for image in lib:
            state = pg.locateAllOnScreen(r"D:\programacion\bot_juegos\{}".format(image),confidence=.8)
            if state != None:
                cor = pg.locateCenterOnScreen(r"D:\programacion\bot_juegos\{}".format(image),confidence=.8)
                if cor != None:
                    pg.click(cor)
                    time.sleep(2)   
    return ":)"

print(multiple())