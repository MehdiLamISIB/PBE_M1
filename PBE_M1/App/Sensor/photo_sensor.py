import RPi.GPIO as GPIO
import time
ldr_pin=22
GPIO.setmode(GPIO.BCM)

GPIO.setup(ldr_pin,GPIO.IN)

def getPhotoResistorSignal():
    return GPIO.input(ldr_pin)

"""
while True:
    try:
        print("la valeur de la résistance est ",GPIO.input(ldr_pin))
        time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
"""