import network
import utime
import machine

from timeout import Timeout
import wifi_config

led = machine.Pin(5, machine.Pin.OUT)
led.value(1)


net = network.WLAN(network.STA_IF)
net.active(True)
net.connect(wifi_config.wifi_ssid, wifi_config.wifi_pw)

connectTimeout = Timeout(10000)

while not net.isconnected():
    led.value(not led.value())
    utime.sleep_ms(100)
    if connectTimeout.hasExpired():
        machine.reset()


led.value(0)

print(net.ifconfig())

import user
