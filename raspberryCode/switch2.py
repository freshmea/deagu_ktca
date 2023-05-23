import RPi.GPIO as GPIO 
import time

def loop(switch1, switch2):
    prev_time1 = time.time()
    prev_time2 = time.time()
    while True:
        if GPIO.input(switch1) == False and time.time()-prev_time1 > 1:
            print(switch1, ' switch Pushed')
            prev_time1 = time.time()
        if GPIO.input(switch2) == False and time.time()-prev_time2 > 1:
            print(switch2, ' switch Pushed')
            prev_time2 = time.time()

def main():
    switch1 = 3
    switch2 = 4

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(switch1, GPIO.IN)
    GPIO.setup(switch2, GPIO.IN)
    print('RaspberryPi switch2 - python')
    
    try:
        loop(switch1, switch2)  
    except KeyboardInterrupt:
        GPIO.cleanup()
    except :
        GPIO.cleanup()


if __name__ == '__main__':
    main()