from gpiozero import Servo
from time import sleep
import math as mt
def check_servo_movement(servo):
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)


def cos_move_servo(servo,freq,val):
    servo.value=mt.cos(freq*val)
    print(servo.value)
    val=val+0.1
    return val
def linear_move(servo,val,increment):
    if(val>1):
        val=-1
    servo.value=val
    val=val+increment
    return val

"""
val=-1

servo=Servo(14)
try:
    while True:
        val=cos_move_servo(servo,10,val)
        #val=linear_move(servo,val,0.1)
        sleep(0.2)
except KeyboardInterrupt:
    print("programm stopped")
"""