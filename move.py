import RPi.GPIO as gpio
import time

class Move:
    
    def __init__(self):
        # Pins
        self.en1 = 25
        self.en2 = 27
        self.rightW1 = 17
        self.rightW2 = 22
        self.leftW1 = 23
        self.leftW2 = 24
        self.frontSensor = 21
        self.speed = 50
        # SetUp
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        gpio.setup(self.en1,gpio.OUT)
        gpio.setup(self.en2,gpio.OUT)
        gpio.setup(self.rightW1, gpio.OUT) #right wheels
        gpio.setup(self.rightW2, gpio.OUT)
        gpio.setup(self.leftW1, gpio.OUT) #left wheels
        gpio.setup(self.leftW2, gpio.OUT)
        gpio.setup(self.frontSensor,gpio.IN)
        self.p1 = gpio.PWM(self.en1,1000)
        self.p2 = gpio.PWM(self.en2,1000)
        self.p1.start(self.speed)
        self.p2.start(self.speed)
        self.calibration = False
        self.timeToRotate = 0 #This variale use for turning with angles
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


    def turnLeftByTime(self,sec):
        self.stop()
        gpio.output(self.rightW1, True)
        gpio.output(self.rightW2, False)
        gpio.output(self.leftW1, True)
        gpio.output(self.leftW2, False)
        time.sleep(sec)
        self.stop()
    
    def turnRightByTime(self,sec):
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
            return True

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


