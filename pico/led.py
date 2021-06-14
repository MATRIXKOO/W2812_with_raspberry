from ws2812 import *
from RGBs import *
from random import *
np = ws2812b(60, 0, 22)


def fill_breath(RGB, top_bright):
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


def sig_breath(RGB, top_bright , pixel):
    R = RGB[0]
    G = RGB[1]
    B = RGB[2]
    while True:
           for i in range(1, top_bright, 1):
                np.brightness(i)
                np.set_pixel(pixel, R, G, B) 
                np.show()
                time.sleep(0.01)

            time.sleep(0.05)

            for i in range(top_bright, 1, -1):
                np.brightness(i)
                np.set_pixel(pixel, R, G, B)
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


def sky(RGBs):
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
        time.sleep(0.2)


def bar(RGB, bar_lenth, brightness, sleep_time):
    RGB = RGBs[RGB]
    R = RGB[0]
    G = RGB[1]
    B = RGB[2]
    np.set_pixel_line(0, bar_lenth, R, G,B)
    np.brightness(brightness)
    np.show()
    for pixel in range(bar_lenth, np.num_leds - bar_lenth):
        np.set_pixel_line(pixel - bar_lenth, pixel, 0, 0,0)
        np.set_pixel_line(pixel, pixel + bar_lenth, R, G,B)
        np.show()
        time.sleep(sleep_time)
    np.set_pixel_line(np.num_leds - bar_lenth - 1, np.num_leds - 1, 0,0,0)
    time.sleep(sleep_time)
    np.show()


def bar_test():
    while True:
        bar("Blue", 5, 100, 0.005)
        bar("Red", 5, 100, 0.005)
        bar("Green", 5, 100, 0.005)


class Timer:
    def __init__(self, np, minute_hand , second_hand, countdown_time):
        self.np = np
        self.minute_hand = minute_hand
        self.second_hand = second_hand
        self.countdown_time = countdown_time
        self.minute = countdown_time // 60
        self.second = countdown_time - (self.minute * 60)

        if(countdown_time > 3600):
            print("Error")
            while Ture:
                pass

    def set_minute(self):
        RGB = RGBs[self.minute_hand]
        R = RGB[0]
        G = RGB[1]
        B = RGB[2]
        self.np.set_pixel_line(0, self.minute - 1 , R, G,B)

    def set_second(self):
        RGB = RGBs[self.second_hand]
        R = RGB[0]
        G = RGB[1]
        B = RGB[2]
        self.np.set_pixel_line(0, self.second - 1, R, G,B)

    def start(self):
        print(self.minute, self.second)
        while self.second != 0 or self.minute != 0:

            if self.minute != 0 and self.second == 0:
                self.minute -= 1
                self.second = 60
                print(self.minute, self.second)

            np.reset()
            self.set_second()
            self.set_minute()
            time.sleep(1)
            self.np.show()
            self.second -= 1
            print(self.minute, self.second)
        np.reset()
        self.np.show()
