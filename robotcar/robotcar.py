
import BlynkLib
import time
import math

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
       
    def __init__(self):
        ## Assumes blynk joystick runs from -128->128 on x/y axis        
        self.maxval = 128

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

blynk.run()
