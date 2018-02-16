import machine
import neopixel
import utime


class CountdownTimer:
    def __init__(self, time_ms):
        self.reset(time_ms)

    def reset(self, time_ms):
        self.duration_ms = time_ms
        self.start_time = utime.ticks_ms()
        self.expired = False

    def elapsedTime(self):
        if self.expired:
            return self.duration_ms
        return utime.ticks_diff(utime.ticks_ms(), self.start_time)

    def hasExpired(self):
        if not self.expired:
            self.expired = self.elapsedTime() > self.duration_ms
        return self.expired

    def getProgress(self):
        if self.expired:
            return 1.0
        return float(self.elapsedTime()) / float(self.duration_ms)


np = neopixel.NeoPixel(machine.Pin(13), 17)


def lerp(a, b, control):
    return a + control * (b - a)


def lerpRGB(rgb1, rgb2, control):
    return (int(lerp(rgb1[0], rgb2[0], control)),
            int(lerp(rgb1[1], rgb2[1], control)),
            int(lerp(rgb1[2], rgb2[2], control)))


def setColourAll(rgb):
    np.fill(rgb)
    np.write()
    pass


def tranistionTo(rgb, time_ms):
    pass


def goDisco():
    pass


def doLightControl():
    pass
