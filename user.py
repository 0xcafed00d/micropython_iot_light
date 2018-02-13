import utime

from microWebSrv import MicroWebSrv
from colours import Colours
import lightcontrol

lightcontrol.setColourAll((0, 0, 0))


def httpHandlerLightGet(httpClient, httpResponse):
    q = httpClient.GetRequestQueryString()
    if q.startswith("command="):
        q = q[len("command="):].lower()
        if q == "disco":
            lightcontrol.goDisco()
        else:
            print(q)
            rgb = Colours.get(q)
            if rgb is not None:
                lightcontrol.tranistionTo(rgb, 1000)

    httpResponse.WriteResponseOk()


routeHandlers = [
    ("/light",	"GET",	httpHandlerLightGet)
]

srv = MicroWebSrv(routeHandlers=routeHandlers)
srv.Start(threaded=True)

while True:
    utime.sleep_ms(10)
    lightcontrol.doLightControl()
