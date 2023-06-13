"""
import servo_control as serv_ctrl
from gpiozero import Servo
from time import sleep
from multiprocessing import Process
import sys
servo_left=Servo(15)
servo_right=Servo(14)
pr1= Process(target=serv_ctrl.check_servo_movement(servo_left))
pr2=Process(target=serv_ctrl.check_servo_movement(servo_right))
pr1.start()
pr2.start()
sys.exit()
"""

from gpiozero import Servo
from time import sleep
import sys
srv1=Servo(20)#Servo(23)
srv2=Servo(21)#Servo(24)


srv1.detach()
srv2.detach()

def HelloMove():
    srv1.value=-1
    srv2.value=1
    i=0
    while i!=3:
        srv1.value=srv1.value+0.1
        print(srv1.value)
        srv2.value=srv2.value-0.1
        if srv1.value>=1:
            srv1.value=-1
            i=i+1
        if srv2.value<=-1:
            srv2.value=1
        sleep(0.1)
    srv1.detach()
    srv2.detach()


def InverseMove():
    srv1.value=-1
    srv2.value=-1
    i=0
    while i!=3:
        srv1.value=srv1.value+0.1
        print(srv1.value)
        srv2.value=srv2.value+0.1
        if srv1.value>=1:
            srv1.value=-1
            i=i+1
        if srv2.value>=1:
            srv2.value=-1
        sleep(0.05)
    srv1.detach()
    srv2.detach()


def TranslateMove(servo,begin,end,step,timestep):
    servo.value=begin
    while servo.value<=end-step:
        servo.value=servo.value+step
        sleep(timestep)
    servo.value=begin


def OneOneMove():
    srv1.value=-1
    srv2.value=-1
    i=0
    while i!=3:
        TranslateMove(srv1,-1,1,0.1,0.05)
        TranslateMove(srv2,-1,1,0.1,0.05)
        i=i+1
        #sleep(0.05)
    srv1.detach()
    srv2.detach()


def ZigZagMove():
    srv1.value=-1
    srv2.value=-1
    i=0
    while i!=3:
        TranslateMove(srv1,-1,1,0.5,0.05)
        TranslateMove(srv2,-1,1,0.5,0.05)
        i=i+1
    srv1.detach()
    srv2.detach()

ZigZagMove()