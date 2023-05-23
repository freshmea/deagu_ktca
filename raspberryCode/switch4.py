import RPi.GPIO as GPIO 
import time
from switch_module import Switch

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