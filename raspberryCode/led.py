import RPi.GPIO as GPIO 
import time

led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
print('RaspberryPi led - Blink, python')
try:
    while True:
        GPIO.output(led, True) # C code :true, 
        time.sleep(0.5)
        GPIO.output(led, False) # C code :false
        time.sleep(0.5)
        
except KeyboardInterrupt:
    GPIO.cleanup()
except :
    GPIO.cleanup()

