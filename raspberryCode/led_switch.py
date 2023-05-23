import RPi.GPIO as GPIO 
import time


led = 21
switch = 3
flag = True
ptime = time.time()

def mycallback(pin):
    global flag, ptime

    if flag and time.time() - ptime > 0.1:
        flag = False
        ptime = time.time()
        print(flag)
    elif time.time() - ptime > 0.1:
        flag = True
        ptime = time.time()
        print(flag)

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

GPIO.setup(switch, GPIO.IN)
GPIO.add_event_detect(switch, GPIO.RISING, callback = mycallback)

print('RaspberryPi led - Blink, python')
try:
    while True:
        if flag:
            GPIO.output(led, True) # C code :true, 
            time.sleep(1)
            GPIO.output(led, False) # C code :false
            time.sleep(1)
        else:
            GPIO.output(led, False)
        
except KeyboardInterrupt:
    GPIO.cleanup()
except :
    GPIO.cleanup()

