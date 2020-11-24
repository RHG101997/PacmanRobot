import time
import RPi.GPIO as gpio
from encoder import Encoder

class Move:
    
    def __init__(self, config):
        # Pins
        self.en1 = int(config["en1"]) if "en1" in config else 25
        self.en2 = int(config["en2"]) if "en2" in config else 27
        self.rightW1 =int(config["rightW1"]) if "rightW1" in config else  17
        self.rightW2 = int(config["rightW2"]) if "rightW2" in config else  22
        self.leftW1 = int(config["leftW1"]) if "leftW1" in config else  23
        self.leftW2 = int(config["leftW2"]) if "leftW2" in config else 24
        # Encoder added
        self.enc1 = Encoder(20,21)

        self.frontSensor = int(config["frontSensor"]) if "frontSensor" in config else 21
        self.speed = int(config["speed"]) if "speed" in config else 50
        self.config = config
        # SetUp
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        gpio.setup(self.en1, gpio.OUT)
        gpio.setup(self.en2, gpio.OUT)
        gpio.setup(self.rightW1, gpio.OUT) #right wheels
        gpio.setup(self.rightW2, gpio.OUT)
        gpio.setup(self.leftW1, gpio.OUT) #left wheels
        gpio.setup(self.leftW2, gpio.OUT)
        gpio.setup(self.frontSensor, gpio.IN)
        self.p1 = gpio.PWM(self.en1, 1000)
        self.p2 = gpio.PWM(self.en2, 1000)
        self.p1.start(self.speed)
        self.p2.start(self.speed)
        # Calibration settings
        if(config.getboolean("calibrate")):
            self.calibrateRobot()
        else:
            self.calibration = True
            self.timeToRotate = float(config["default_calibration"])
        # Initialization for motors 
        self.stop()
        time.sleep(4)



    def forward(self):
        if self.checkFront():
            print("Object detected")
            self.stop()
        else:
            gpio.output(self.rightW1, False)
            gpio.output(self.rightW2, True)
            gpio.output(self.leftW1, True)
            gpio.output(self.leftW2, False) 
    def reverse(self):
        gpio.output(self.rightW1, True)
        gpio.output(self.rightW2, False)
        gpio.output(self.leftW1, False)
        gpio.output(self.leftW2, True)
    def stop(self):
        gpio.output(self.rightW1, False)
        gpio.output(self.rightW2, False)
        gpio.output(self.leftW1, False)
        gpio.output(self.leftW2, False)
    def turnLeft(self):
        self.stop()
        gpio.output(self.rightW1, True)
        gpio.output(self.rightW2, False)
        gpio.output(self.leftW1, True)
        gpio.output(self.leftW2, False)
    def turnRight(self):
        self.stop()
        gpio.output(self.rightW1, False)
        gpio.output(self.rightW2, True)
        gpio.output(self.leftW1, False)
        gpio.output(self.leftW2, True)
    def turnLeftByTime(self, sec):
        self.stop()
        gpio.output(self.rightW1, True)
        gpio.output(self.rightW2, False)
        gpio.output(self.leftW1, True)
        gpio.output(self.leftW2, False)
        time.sleep(sec)
        self.stop()
    def turnRightByTime(self, sec):
        self.stop()
        gpio.output(self.rightW1, False)
        gpio.output(self.rightW2, True)
        gpio.output(self.leftW1, False)
        gpio.output(self.leftW2, True)
        time.sleep(sec)
        self.stop()
    def turnRightByAngle(self, angle):
        if(not self.calibration):
            print("Calibartion Required")
        else:
            turning_time = (angle*self.timeToRotate)/360
            self.turnRightByTime(turning_time) 
    def turnLeftByAngle(self, angle):
        if(not self.calibration):
            print("Calibartion Required")
        else:
            turning_time = (angle*self.timeToRotate)/360
            self.turnLeftByTime(turning_time)
    def changeSpeed(self, speed):
        self.speed = speed
        self.p1.ChangeDutyCycle(speed)
        self.p2.ChangeDutyCycle(speed)

    def checkFront(self):
        if gpio.input(self.frontSensor):
            return False
        else:
            return False # change so try forward

    # Added encoders to Motors
    def moveBy(self,steps):
        while(steps >= self.enc1.read()):
            self.forward()
        self.stop()


    def calibrateRobot(self):
        print("Begin Calibration Procedure\nPlace Object in front of sensor")
        while(not self.checkFront()): 
            print("Waiting")
            time.sleep(2) 
        begin_time = time.time()
        self.turnLeft()
        time.sleep(0.5) #allowing the car to move
        # Waiting for next sensor update
        while(not self.checkFront()):
            pass
        self.stop()
        # Calculate time
        self.timeToRotate = time.time()-begin_time
        self.calibration = True
        print("Calibration Completed 360 Time: "+str(self.timeToRotate))
        time.sleep(5)


