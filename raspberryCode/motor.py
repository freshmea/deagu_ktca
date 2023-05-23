import RPi.GPIO as gpio
import time
from switch_module import Switch

pin_positive = 18

gpio.setmode(gpio.BCM)
gpio.setup(pin_positive, gpio.OUT)
dcm = gpio.PWM(pin_positive, 50)

dcm.start(0)

try:
    Switch.switchs.append(Switch(3))
    Switch.switchs.append(Switch(4))
    while True:
        if Switch.switchs[0].switch_input():
            for i in range(0, 30, 5):
                dcm.ChangeDutyCycle(i)
                time.sleep(1)
                print(i)
        elif Switch.switchs[1].switch_input():
            gpio.output(pin_positive, False)
                
except KeyboardInterrupt:
    gpio.cleanup()