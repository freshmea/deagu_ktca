import RPi.GPIO as gpio 
import time
from switch_module import Switch

def loop(Buzz, lMelody, switchs, led1, led2):
    flag = False
    while True:
        for switch in switchs:
            print(flag)
            if switch.switch_input():
                if switch.pin == 3:
                    flag = True
                elif switch.pin == 4:
                    flag = False
        if flag:    
            Buzz.start(50)
            Buzz.ChangeFrequency(lMelody[0])
            gpio.output(led1, True)
            gpio.output(led2, False)
            time.sleep(0.3)
            Buzz.ChangeFrequency(lMelody[2])
            gpio.output(led1, False)
            gpio.output(led2, True)
            time.sleep(0.3)
        else:
            Buzz.stop()
            gpio.output(led1, False)
            gpio.output(led2, False)
            
            
            

def main():
    piezo = 13
    led1 = 21
    led2 = 20
    lMelody = [131, 147, 165, 175, 196, 220, 247, 262]

    gpio.setmode(gpio.BCM)
    gpio.setup(piezo, gpio.OUT)
    gpio.setup(led1, gpio.OUT)
    gpio.setup(led2, gpio.OUT)
    
    Buzz = gpio.PWM(piezo, 440)
    Switch.switchs.append(Switch(3))
    Switch.switchs.append(Switch(4))
    print('RaspberryPi piezo - python')
    
    try:
        loop(Buzz, lMelody, Switch.switchs, led1, led2)
    except KeyboardInterrupt:
        gpio.cleanup()
    except :
        gpio.cleanup()


if __name__ == '__main__':
    main()