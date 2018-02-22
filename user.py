import utime
import _thread

from microWebSrv import MicroWebSrv
from colours import Colours
import lightcontrol

lc = lightcontrol.LightControl(13, 16)
lc.setColourAll((0, 0, 0))

sync = _thread.allocate_lock()


def httpHandlerLightGet(httpClient, httpResponse):
    q = httpClient.GetRequestQueryString()
    if q.startswith("command="):
        q = q[len("command="):].lower()
        print(q)
        if q == "disco":
            with sync:
                lc.goDisco()
        elif q == "random":
            with sync:
                lc.goRandom()
        else:
            rgb = Colours.get(q)
            if rgb is not None:
                with sync:
                    lc.tranistionTo(rgb, 1000)

    httpResponse.WriteResponseOk()


routeHandlers = [
    ("/light",	"GET",	httpHandlerLightGet)
]

srv = MicroWebSrv(routeHandlers=routeHandlers)
srv.Start(threaded=True)


def lightControlThread():
    while True:
        utime.sleep_ms(50)
        with sync:
            lc.doLightControl()


_thread.start_new_thread(lightControlThread, ())

while True:
    utime.sleep(10)
