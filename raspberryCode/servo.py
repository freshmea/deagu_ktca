import RPi.GPIO as gpio
import time
from switch_module import Switch

servo = 12

gpio.setmode(gpio.BCM)
gpio.setup(servo, gpio.OUT)
ser = gpio.PWM(servo, 50)

ser.start(7.5)

try:
    # Switch.switchs.append(Switch(3))
    # Switch.switchs.append(Switch(4))
    while True:
        # if Switch.switchs[0].switch_input():
        ser.ChangeDutyCycle(2.3)
        time.sleep(2)
        ser.ChangeDutyCycle(7)
        time.sleep(2)
        ser.ChangeDutyCycle(12)
        time.sleep(2)
        # elif Switch.switchs[1].switch_input():
        #     gpio.output(servo, False)
                
except KeyboardInterrupt:
    gpio.cleanup()