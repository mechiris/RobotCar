
import BlynkLib
import time
import math

class RobotCar():

    @blynk.VIRTUAL_WRITE(1)
    def my_write_handler(value):
            print('Current V1 value: {}'.format(value))

    @blynk.VIRTUAL_WRITE(2)
    def my_write_handler(value):
            print('Current V2 value: {}'.format(value))

    @blynk.VIRTUAL_WRITE(3)
    def my_write_handler(value):
            print('Current V3 value: {}'.format(value))

    def updateSpeedVectors(x=self.x,y=self.y):
        self.x = x
        self.y = y
        self.r = math.sqrt(x^2 + y^2) / self.maxval^2


    def start(self):
        blynk.run()
       
    def __init__(self):
        ## Assumes blynk joystick runs from -128->128 on x/y axis        
        self.maxval = 128

        self.x = 0
        self.y = 0
        self.r = 0

        with open('creds.txt', 'r') as f:
            self.BLYNK_AUTH = f.readline()
        # Initialize Blynk
        blynk = BlynkLib.Blynk(BLYNK_AUTH)


