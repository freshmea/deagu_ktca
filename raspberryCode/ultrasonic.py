import RPi.GPIO as gpio
import time

def measure():
    gpio.output(pinTrigger, True)
    time.sleep(0.00001)
    gpio.output(pinTrigger, False)
    start = time.time()
    
    while gpio.input(pinEcho) == False:
        start = time.time()
    while gpio.input(pinEcho) == True:
        stop = time.time()
        
    elapsed = stop - start
    distance = (elapsed * 19000)/2
    
    return distance

pinTrigger = 0
pinEcho = 1

gpio.setmode(gpio.BCM)
gpio.setup(pinTrigger, gpio.OUT)
gpio.setup(pinEcho, gpio.IN)

try:
    while True:
        distance = measure()
        print(f'distance: {distance} cm ')
        time.sleep(1)
except KeyboardInterrupt:
    gpio.cleanup()