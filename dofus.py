import time 
import pyautogui as pg 


def dofus():
    time.sleep(3)
    ruta = r"D:\programacion\bot_juegos\roble.png"
    state = pg.locateAllOnScreen(ruta, confidence = .8)
    if state != None:
        cor = pg.locateCenterOnScreen(ruta)
        pg.click(cor)
        return ":)"
    return ":("


print(dofus())