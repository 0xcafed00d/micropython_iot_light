import machine
from microWebSrv import MicroWebSrv
import time
import neopixel

led = machine.Pin(5, machine.Pin.OUT)
led.value(0)

np = neopixel.NeoPixel(machine.Pin(13), 17)
np.fill((0, 0, 0))
np.write()

import colours


def _httpHandlerLightGet(httpClient, httpResponse):
    q = httpClient.GetRequestQueryString()
    if q.startswith("command="):
        q = q[len("command="):].lower()
        print(q)
        rgb = colours.Colours.get(q)
        print(rgb)
        if rgb is not None:
            np.fill(rgb)
            np.write()

    httpResponse.WriteResponseOk()


routeHandlers = [
    ("/light",	"GET",	_httpHandlerLightGet)
]

srv = MicroWebSrv(routeHandlers=routeHandlers)
srv.Start(threaded=False)
