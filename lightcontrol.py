import machine
import neopixel
import utime
import math
from timetools import CountdownTimer


def lerp(a, b, control):
    return a + control * (b - a)


def lerpRGB(rgb1, rgb2, control):
    return (int(lerp(rgb1[0], rgb2[0], control)),
            int(lerp(rgb1[1], rgb2[1], control)),
            int(lerp(rgb1[2], rgb2[2], control)))


class LightControl:

    def __init__(self, pin, count):
        self.np = neopixel.NeoPixel(machine.Pin(pin), count)
        self.timer = CountdownTimer(0)
        self.begin_rgb = (0, 0, 0)
        self.end_rgb = (0, 0, 0)
        self.discoMode = False
        self.phases = [0.0, 0.0, 0.0]
        self.rates = [0.1, 0.2, 0.3]

    def setColourAll(self, colour):
        self.np.fill(colour)
        self.np.write()

    def tranistionTo(self, colour, time_ms):
        self.discoMode = False
        self.begin_rgb = self.end_rgb
        self.end_rgb = colour
        self.timer.reset(time_ms)

    def goDisco(self):
        self.setColourAll((0, 0, 0))
        self.discoMode = True
        self.begin_rgb = (0, 0, 0)
        self.end_rgb = (0, 0, 0)

    def doDisco(self):
        for p in range(0, 16):
            r = abs(math.sin(math.pi/16 * p + self.phases[0])) * 255
            g = abs(math.sin(math.pi/16 * p + self.phases[1])) * 255
            b = abs(math.sin(math.pi/16 * p + self.phases[2])) * 255

            self.phases[0] += 0.01
            self.phases[1] += 0.001
            self.phases[2] += 0.03

            self.np[p] = (int(r), int(g), int(b))

        self.np.write()

    def doFade(self):
        newrgb = lerpRGB(self.begin_rgb, self.end_rgb,
                         self.timer.getProgress())
        self.setColourAll(newrgb)

    def doLightControl(self):
        if self.discoMode:
            self.doDisco()
        else:
            self.doFade()
