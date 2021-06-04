#pick color by win32 API
#from https://blog.csdn.net/xugexuge/article/details/87537765
from ctypes import *

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
    print(get_color(0,0))