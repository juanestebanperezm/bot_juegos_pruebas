import cv2 
import pyautogui as pg 
import time 


def bot_():
    #Mientras hago el cambio de ventana
    time.sleep(2)
    ruta = r"D:\programacion\bot_juegos\roble.png"
    ruta_d = r"D:\programacion\bot_juegos\ortiga.png"
    image_prueba = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
    needle_im = cv2.imread(ruta_d,cv2.IMREAD_UNCHANGED)
    
    resultado = cv2.matchTemplate(image_prueba, needle_im, cv2.TM_SQDIFF_NORMED)
    return resultado




print(bot_())