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
        

def loop(switchs):
    while True:
        for switch in switchs:
            if switch.switch_input():
                print(switch.pin, ' switch Pushed')

def main():
    GPIO.setmode(GPIO.BCM)
    Switch.switchs.append(Switch(3))
    Switch.switchs.append(Switch(4))
    print('RaspberryPi switch3 - python')
    
    try:
        loop(Switch.switchs)  
    except KeyboardInterrupt:
        GPIO.cleanup()
    except :
        GPIO.cleanup()


if __name__ == '__main__':
    main()