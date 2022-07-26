import pyautogui as pg
import time 
import os
def aim():
    time.sleep(2)
    ruta = [i for i in os.listdir(r"D:\programacion\bot_juegos") if i.endswith(".png") ]
    while True:
        for image in ruta:
            state = pg.locateAllOnScreen(r"D:\programacion\bot_juegos\{}".format(image),confidence=.8)
            if state != None:
                cor = pg.locateCenterOnScreen(r"D:\programacion\bot_juegos\{}".format(image),confidence=.8)
                if cor != None:
                    pg.click(cor)
                    time.sleep(.2)
    return (":)")




print(aim())