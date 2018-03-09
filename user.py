import utime

import nbwebserver
from colours import Colours
import lightcontrol

lc = lightcontrol.LightControl(13, 16)
lc.setColourAll((0, 0, 0))


def lightHandler(request, response):
    command = request.query.get("command")
    if command is not None:
        print(command)
        if command == "disco":
            lc.goDisco()
        elif command == "random":
            lc.goRandom()
        else:
            rgb = Colours.get(command)
            if rgb is not None:
                lc.tranistionTo(rgb, 1000)

    response.sendOK()


srv = nbwebserver.WebServer()
srv.AddHandler("/light", lightHandler)
srv.Start()


while True:
    utime.sleep_ms(10)
    srv.Update()
    lc.doLightControl()
