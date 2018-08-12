
import BlynkLib
import time
import math
from dual_g2_hpmd_rpi import motors, MAX_SPEED

with open('creds.txt', 'r') as f:
    BLYNK_AUTH = f.readline()
# Initialize Blynk
global blynk 
blynk = BlynkLib.Blynk(BLYNK_AUTH)

class RobotCar():
    def receiveX1Value(self,value):
            print('Current X1 value: ' + str(value))
            value = int(value)
            self.x1 = value
            self.updateMotorSpeeds()

    def receiveX2Value(self,value):
            print('Current X2 value: ' + str(value))
            value = int(value)
            self.x2 = value
            self.updateMotorSpeeds()

    def updateMotorSpeeds(self):
        self.vel_l = MAX_SPEED * self.x1 / self.maxval 
        self.vel_r = MAX_SPEED * self.x2 / self.maxval 

        motors.motor1.setSpeed(self.vel_l)
        motors.motor2.setSpeed(self.vel_r)
       
    def __init__(self):
        ## Assumes blynk joystick runs from -128->128 on x/y axis        
        self.maxval = 128
        motors.enable()

        self.vel_r = 0
        self.vel_l = 0

        self.x1 = 0
        self.x2 = 0 

rc = RobotCar()

@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
        rc.receiveX1Value(value)

@blynk.VIRTUAL_WRITE(3)
def my_write_handler(value):
        rc.receiveX2Value(value)

try:
    blynk.run()
finally:
    motors.setSpeeds(0, 0)
    motors.disable()
