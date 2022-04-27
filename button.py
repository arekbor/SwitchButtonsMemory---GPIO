import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED = 25

switches = {
    4: False,
    17: False,
    18: False,
    22: False,
    23: False,
    24: False,
}

for key in switches:
    GPIO.setup(key,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)

def printSwitches():
    for key in switches:
        print(key,'->',switches[key])

def Switch():
    for pin in switches:
        if GPIO.input(pin) == 0 and switches.get(pin) == False:
            time.sleep(0.2)
            if GPIO.input(pin) == True:
                switches[pin] = True
                printSwitches()
        if GPIO.input(pin) == 0 and switches.get(pin) == True:
            time.sleep(0.2)
            if GPIO.input(pin) == True:
                switches[pin] = False
                printSwitches()
x = 1
def blinkLed():
    for x in range(5):
        GPIO.output(LED,True)
        time.sleep(0.5)
        GPIO.output(LED,False)
        time.sleep(0.5)

def resetButtons():
    for pin in switches:
        switches[pin] = False
 
while True:
    Switch()
    if switches.get(4) == True and switches.get(18) == True and switches.get(24) == True:
        blinkLed()
        resetButtons()
