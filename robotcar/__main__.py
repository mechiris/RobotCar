import sys
from robotcar import RobotCar

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    
    RC = RobotCar()
    RC.start()

if __name__ == "__main__":
    main()
