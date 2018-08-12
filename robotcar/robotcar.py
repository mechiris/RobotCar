
import BlynkLib
import time
import math
import math
from dual_g2_hpmd_rpi import motors#, MAX_SPEED

MAX_SPEED=128

with open('creds.txt', 'r') as f:
    BLYNK_AUTH = f.readline()
# Initialize Blynk
global blynk 
blynk = BlynkLib.Blynk(BLYNK_AUTH)

class RobotCar():
    def receiveXValue(self,value):
            #print('Current X value: ' + str(value))
            value = int(value)
            self.x = value
            self.updateMotorSpeeds()

    def receiveYValue(self,value):
            #print('Current Y value: ' + str(value))
            value = int(value)
            self.y = value
            self.updateMotorSpeeds()

    def updateMotorSpeeds(self):
        self.r = math.sqrt(self.x**2 + self.y**2) 
        if self.r > 0:
            theta = math.degrees(math.asin(self.x/self.r))
        else:
            theta = 0

        if self.x >= 0:
            if self.y > 0:
                ## Quadrant 1
                v_m1 = MAX_SPEED * self.r / self.maxval 
                v_m2 = MAX_SPEED * self.y * self.r / self.maxval**2
            else:
                ## Quadrant 2
                v_m1 = -1 * MAX_SPEED * self.r / self.maxval
                v_m2 = MAX_SPEED * self.y * self.r / self.maxval**2
        else:
            if self.y > 0:
                ## Quadrant 3
                v_m2 = -1 * MAX_SPEED * self.r / self.maxval 
                v_m1 = MAX_SPEED * self.y * self.r / self.maxval**2
            else:
                ## Quadrant 4
                v_m2 = MAX_SPEED * self.r / self.maxval
                v_m1 = MAX_SPEED * self.y * self.r / self.maxval**2
        #v_m1 = int(MAX_SPEED *  theta * self.r/self.maxval)
        #v_m2 = int(MAX_SPEED *  theta * self.r/self.maxval)
        print ("velocities: " + str(v_m1) + ',' + str(v_m2) + ',' + str(theta))
        motors.motor1.setSpeed(int(v_m1))
        motors.motor2.setSpeed(int(v_m2))
       
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
