'''pick color by win32 API
reference:
https://blog.csdn.net/xugexuge/article/details/87537765
https://blog.csdn.net/weixin_34185320/article/details/91810157
'''
from ctypes import *
import os,time
import pyautogui as pag

def get_pos():
    x,y = pag.position()
    return x,y
    

def get_color(x,y):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)
    pixel = gdi32.GetPixel(hdc,x,y)

    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    return [r,g,b]

if __name__ == '__main__':
    while True:
        x,y = get_pos()
        print(get_color(x,y))
        time.sleep(1)
    print("ending")