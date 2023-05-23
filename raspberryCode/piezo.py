import RPi.GPIO as gpio 
import time

def loop(Buzz, lMelody):
    while True:
        Buzz.start(50)
        for i in lMelody:
            Buzz.ChangeFrequency(i)
            time.sleep(0.3)
        Buzz.stop()
        time.sleep(5)
            
            

def main():
    piezo = 13
    lMelody = [131, 147, 165, 175, 196, 220, 247, 262]

    gpio.setmode(gpio.BCM)
    gpio.setup(piezo, gpio.OUT)
    Buzz = gpio.PWM(piezo, 440)
    print('RaspberryPi piezo - python')
    
    try:
        loop(Buzz, lMelody)  
    except KeyboardInterrupt:
        gpio.cleanup()
    except :
        gpio.cleanup()


if __name__ == '__main__':
    main()