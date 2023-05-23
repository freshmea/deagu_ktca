import RPi.GPIO as GPIO 
import time

def loop(led1, led2):
    prev_time = time.time()
    led_state = 0
    while True:
        if time.time() - prev_time < 1:
            if led_state == 0:
                GPIO.output(led1, True)
                GPIO.output(led2, False)
                led_state = 1
        elif time.time() - prev_time < 2:
            if led_state == 1:
                GPIO.output(led1, False)
                GPIO.output(led2, True)
                led_state = 0
        else:
            prev_time = time.time()

def main():
    led1 = 21
    led2 = 20

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)
    print('RaspberryPi led2 - Blink, python')
    
    try:
        loop(led1, led2)  
    except KeyboardInterrupt:
        GPIO.cleanup()
    except :
        GPIO.cleanup()


if __name__ == '__main__':
    main()