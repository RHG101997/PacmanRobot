from imutils.video import VideoStream
from target import Target
import cv2
import imutils


class Vision:
    def __init__(self,config,move,target):
        # Camera stream
        self.vs = VideoStream(usePiCamera=1).start()
        # Movement
        self.move = move
        # Current Target
        self.target = target
        #GUI(default is False)
        self.gui = config.getboolean("gui") if "gui" in config else False
        
        # Angle(Default is 54(raspberry cam))
        self.camera_horizontal_view = int(config["camera_horizontal_view"]) if "camera_horizontal_view" in config else 54
        # Frame Ratio(Default is 600x480)
        self.frameWidth =int(config["frameWidth"]) if "frameWidth" in config else 600
        self.frameLength = int(config["frameLength"]) if "frameLength" in config else 480
        self.frameCenter = (self.frameWidth/2,self.frameLength/2)
        self.config = config


    def analyseFrame(self):
        frame = self.vs.read()
        # Check if frame avaible
        if frame is None:
            self.target.onScreen = False
            return frame
        frame = cv2.resize(frame, (self.frameWidth,self.frameLength))
        #Blur image for less noice
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        # create a mask of black and white
        mask = cv2.inRange(hsv, self.target.colorLower, self.target.colorUpper)
        # eroding and dilatation(helps remove smaller blob found in frame)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2) 
        # Getting countor
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        # make sure the information is from correct version
        cnts = imutils.grab_contours(cnts)
        # if found at least 1 contour
        if len(cnts) > 0:
            # Get the largest contour in mask
            c = max(cnts, key=cv2.contourArea)
            # x,y and radius
            self.target.getInfo(cv2.minEnclosingCircle(c))
            self.target.onScreen = True
            return frame
        else:
            self.target.onScreen = False
            return frame
    
    ''' Function searches for specifc target around the robot '''
    def search(self,target = self.target):
        self.target = target #assign target to vision class
        # turn while target is not on sight
        while(not target.onScreen):
            frame = self.analyseFrame()
            self.move.turnRightByAngle(20)
        self.followTarget()

    
    def followTarget(self, target = self.target):
        while True:
            frame  = self.analyseFrame()
            if self.target.onScreen:
                offset_dist =self.target.x-self.frameCenter[0]
                angle = (abs(offset_dist)*(self.camera_horizontal_view/2))/(self.frameCenter[0])
                if self.gui: 
                    cv2.circle(frame, (self.target.x, self.target.y), self.target.radius,(0, 255, 255), 2)
                    cv2.line(frame, (self.target.x, self.frameCenter[1]),self.frameCenter,(0, 0, 255),2)

                if(offset_dist < -100 and radius < 60):
                    # turn right
                    self.move.turnRightByAngle(angle)
                elif(offset_dist > 100 and  radius < 60):
                    # turn left
                    self.move.turnLeftByAngle(angle) 
                elif(radius < 60):
                    #forward
                    self.move.forward()
                elif(radius > 80):
                    # Reverse
                    self.move.reverse() 
                else:
                    # Stop
                    self.move.stop()
            else:
                self.search() # search if object not found     
            if self.gui:
                #Show the the object in video frame 
                cv2.imshow("Frame", frame)
                key = cv2.waitKey(1) & 0xFF
                # if the 'q' key is pressed, stop the loop
                if key == ord("q"):
	                break


    def showGUI(self):
        self.gui = True
    





        