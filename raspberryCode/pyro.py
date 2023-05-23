import RPi.GPIO as gpio
import time

pir = 26

gpio.setmode(gpio.BCM)
gpio.setup(pir, gpio.IN)

try:
    while True:
        if gpio.input(pir) == False:
            print('Detect')
            time.sleep(0.5)
        else:
            print('no Detect')
except KeyboardInterrupt:
    gpio.cleanup()