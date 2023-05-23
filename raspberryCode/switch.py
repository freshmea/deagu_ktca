import RPi.GPIO as GPIO 
import time

def loop(switch):
    prev_time = time.time()
    while True:
        if GPIO.input(switch) == False and time.time()-prev_time > 10:
            print(switch, ' switch Pushed')
            prev_time = time.time()

def main():
    switch = 3

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(switch, GPIO.IN)
    print('RaspberryPi switch - python')
    
    try:
        loop(switch)  
    except KeyboardInterrupt:
        GPIO.cleanup()
    except :
        GPIO.cleanup()


if __name__ == '__main__':
    main()