import utime
import _thread

from microWebSrv import MicroWebSrv
from colours import Colours
import lightcontrol

lc = lightcontrol.LightControl(13, 17)
lc.setColourAll((0, 0, 0))


def httpHandlerLightGet(httpClient, httpResponse):
    q = httpClient.GetRequestQueryString()
    if q.startswith("command="):
        q = q[len("command="):].lower()
        if q == "disco":
            lc.goDisco()
        else:
            print(q)
            rgb = Colours.get(q)
            if rgb is not None:
                lc.tranistionTo(rgb, 1000)

    httpResponse.WriteResponseOk()


routeHandlers = [
    ("/light",	"GET",	httpHandlerLightGet)
]

srv = MicroWebSrv(routeHandlers=routeHandlers)
srv.Start(threaded=True)

while True:
    utime.sleep_ms(10)
    lc.doLightControl()
    print(".", end='')
