import machine
import time
import neopixel

from microWebSrv import MicroWebSrv
from colours import Colours

led = machine.Pin(5, machine.Pin.OUT)
led.value(0)

np = neopixel.NeoPixel(machine.Pin(13), 17)
np.fill((0, 0, 0))
np.write()


def httpHandlerLightGet(httpClient, httpResponse):
    q = httpClient.GetRequestQueryString()
    if q.startswith("command="):
        q = q[len("command="):].lower()
        print(q)
        rgb = Colours.get(q)
        print(rgb)
        if rgb is not None:
            np.fill(rgb)
            np.write()

    httpResponse.WriteResponseOk()


routeHandlers = [
    ("/light",	"GET",	httpHandlerLightGet)
]

srv = MicroWebSrv(routeHandlers=routeHandlers)
srv.Start(threaded=False)
