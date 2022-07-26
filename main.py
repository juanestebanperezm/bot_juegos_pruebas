import pyautogui as pg 
import time 


#Bot de la galleta

def bot():
    time.sleep(2)
    ruta = r'D:\programacion\bot_juegos\cook.png'
    state = pg.locateAllOnScreen(ruta, confidence = 0.8)
    if state != None:
        cor = pg.locateCenterOnScreen(ruta)
        contador = 0
        while contador < 50:
            pg.click(cor)
            contador += 1 
            if contador == 50:
                break
        return ":)"
    return ":("

print(bot())