from ws2812 import *
from RGBs import *
from random import *
np = ws2812b(60, 0, 22)


def breath(RGB):
    R = RGB[0]
    G = RGB[1]
    B = RGB[2]
    while True:
           for i in range(1, 100, 1):
                np.brightness(i)
                np.fill(R, G, B)
                np.show()
                time.sleep(0.01)

            time.sleep(0.05)

            for i in range(100, 1, -1):
                np.brightness(i)
                np.fill(R, G, B)
                np.show()
                time.sleep(0.01)


def RGBs_test():
    for i in RGBs:
        print(RGBs[i])
        tuple_ = RGBs[i]
        np.fill(tuple_[0], tuple_[1], tuple_[2])
        np.show()
        time.sleep(1)


def RGB_test(_RGB):
    RGB = RGBs[_RGB]
    R = RGB[0]
    G = RGB[1]
    B = RGB[2]
    np.set_pixel(1, R, G, B)
    np.show()


#breath(RGBs["LightPink"])
RGB_test("DeepPink")


def sky():
    while True:
        pixel = randint(1, 59)
        random_RGB = choice(list(RGBs))
        random_brightness = randint(100, 255)

        print(pixel, random_RGB)
        RGB = RGBs[random_RGB]
        R = RGB[0]
        G = RGB[1]
        B = RGB[2]

        np.brightness(random_brightness)
        np.set_pixel(pixel, R, G, B)
        np.show()
        time.sleep(0.6)


breath(RGBs["LightSkyBlue"])
