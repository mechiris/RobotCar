
import BlynkLib
import time



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

    def start(self):
        with open('creds.txt', 'r') as f:
            self.BLYNK_AUTH = f.readline()
        # Initialize Blynk
        blynk = BlynkLib.Blynk(BLYNK_AUTH)

        blynk.run()
       
