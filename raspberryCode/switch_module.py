import RPi.GPIO as GPIO 
import time

class Switch:
    switchs = list()
    def __init__(self, pin):
        self.pin = pin
        self.prev_time = time.time()
        GPIO.setup(pin, GPIO.IN)
        
    def switch_input(self):
        ret = GPIO.input(self.pin) == False and time.time()-self.prev_time > 1
        if ret:
            self.prev_time = time.time()
        return ret