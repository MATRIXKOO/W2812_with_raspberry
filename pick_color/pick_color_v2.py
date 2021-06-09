#pick color by screenshot
# from https://github.com/dchen327/ambient-light-color-adjuster/blob/master/light_changer.py

import pyscreenshot as ImageGrab

SCREENSHOT_REGION = (940, 520, 980, 560)
USE_COLORTHIEF = True

def get_color(region, colorthief=True):
    """ Screenshot a portion of the screen and return the rgb tuple of the most dominant color """
    im = ImageGrab.grab(bbox=SCREENSHOT_REGION, backend='mss', childprocess=False)
    if colorthief:
        from colorthief import ColorThief
        im.save('screenshot.png')
        color_thief = ColorThief('screenshot.png')
        color = color_thief.get_color(quality=1)
    else:
        color = im.getpixel((0, 0))
    return color

if __name__ == '__main__':
    #im = ImageGrab.grab()
    #im.show()
    print(get_color(SCREENSHOT_REGION,True))