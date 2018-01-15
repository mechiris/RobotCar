
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
    def receiveXValue(self,value):
            print('Current X value: ' + str(value))
            value = int(value)
            self.x = value
            self.r = math.sqrt(self.x**2 + self.y**2) / self.maxval**2

    def receiveYValue(self,value):
            print('Current Y value: ' + str(value))
            value = int(value)
            self.y = value
            self.r = math.sqrt(self.x**2 + self.y**2) / self.maxval**2

    def updateMotorSpeeds(self):
        motors.motor1.setSpeed(self.x)
        motors.motor2.setSpeed(self.y)
       
    def __init__(self):
        ## Assumes blynk joystick runs from -128->128 on x/y axis        
        self.maxval = 128
        motors.enable()


        self.x = 0
        self.y = 0
        self.r = 0

rc = RobotCar()

@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
        rc.receiveXValue(value)
        #print('Current V2 value: {}'.format(value))

@blynk.VIRTUAL_WRITE(2)
def my_write_handler(value):
        rc.receiveYValue(value)

try:
    blynk.run()
finally:
    motors.setSpeeds(0, 0)
    motors.disable()
