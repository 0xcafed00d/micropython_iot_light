import machine
import neopixel

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
