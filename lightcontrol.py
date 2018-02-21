import machine
import neopixel
import utime
import math
from timetools import CountdownTimer
import urandom


def lerp(a, b, control):
    return a + control * (b - a)


def lerpRGB(rgb1, rgb2, control):
    return (int(lerp(rgb1[0], rgb2[0], control)),
            int(lerp(rgb1[1], rgb2[1], control)),
            int(lerp(rgb1[2], rgb2[2], control)))


colours = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (255, 255, 255)
]


class LightControl:

    def __init__(self, pin, count):
        self.np = neopixel.NeoPixel(machine.Pin(pin), count)
        self.timer = CountdownTimer(0)
        self.begin_rgb = (0, 0, 0)
        self.end_rgb = (0, 0, 0)
        self.doFunc = None

    def setColourAll(self, colour):
        self.np.fill(colour)
        self.np.write()

    def tranistionTo(self, colour, time_ms):
        self.doFunc = self.doFade
        self.begin_rgb = self.end_rgb
        self.end_rgb = colour
        self.timer.reset(time_ms)

    def goDisco(self):
        self.doFunc = self.doDisco
        self.begin_rgb = (0, 0, 0)
        self.end_rgb = (0, 0, 0)

    def goRandom(self):
        self.doFunc = self.doRandom
        self.begin_rgb = (0, 0, 0)
        self.end_rgb = colours[urandom.randint(0, 6)]
        self.timer.reset(5000)

    def doDisco(self):
        pass

    def doFade(self):
        newrgb = lerpRGB(self.begin_rgb, self.end_rgb,
                         self.timer.getProgress())
        self.setColourAll(newrgb)
        if self.timer.hasExpired():
            self.doFunc = None

    def doRandom(self):
        newrgb = lerpRGB(self.begin_rgb, self.end_rgb,
                         self.timer.getProgress())
        self.setColourAll(newrgb)
        if self.timer.hasExpired():
            self.begin_rgb = self.end_rgb
            self.end_rgb = colours[urandom.randint(0, 6)]
            self.timer.reset(5000)

    def doLightControl(self):
        if self.doFunc is not None:
            self.doFunc()
