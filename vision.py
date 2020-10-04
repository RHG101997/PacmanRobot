from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time
import math

class Vision:
    def __init__(self, move, colorLower, colorUpper):
        # Camera stream
        self.vs = VideoStream(usePiCamera=1).start()
        # Movement
        self.move = move
        # target HSV Color
        self.colorLower = colorLower
        self.colorUpper = colorUpper
        #GUI 
        self.gui = False
        # Current Target
        self.target = None
        # Angle
        self.camera_horizontal_view = 54
        # Frame Ratio
        self.frameWidth = 600
        self.frameLength = 480
        self.frameCenter = (self.frameWidth/2,self.frameLength/2)


    def analyseFrame(self):
        frame = self.vs.read()
        # Check if frame avaible
        if frame is None:
            self.target = None
            return frame
        frame = cv2.resize(frame, (self.frameWidth,self.frameLength))
        #Blur image for less noice
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        # create a mask of black and white
        mask = cv2.inRange(hsv, self.colorLower, self.colorUpper)
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
            self.target = cv2.minEnclosingCircle(c)
            return frame
        else:
            self.target = None
            return frame
    

    def followTarget(self):
        while True:
            frame  = self.analyseFrame()
            if self.target is not None:
                ((x, y), radius) = self.target
                offset_dist =int(x)-self.frameCenter[0]
                angle = (abs(offset_dist)*(self.camera_horizontal_view/2))/(self.frameCenter[0])
                if self.gui: 
                    cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                    cv2.line(frame, (int(x), self.frameCenter[1]),self.frameCenter,(0, 0, 255),2)

                if(offset_dist < -100 and radius < 60):
                    if self.move.calibration:
                        self.move.turnRightByAngle(angle)
                    else:
                        print("Right -> Dist: " + str(int(offset_dist)) + "Radius: " + str(int(radius)))

                elif(offset_dist > 100 and  radius < 60):
                    if self.move.calibration:
                        self.move.turnLeftByAngle(angle)
                    else:
                        print("Left -> Dist: " + str(int(offset_dist))+ "Radius: " + str(int(radius)))
                    
                elif(radius < 60):
                    if self.move.calibration:
                        self.move.forward()
                    else:
                        print("Forward -> Dist: " + str(int(offset_dist))+ "Radius: " + str(int(radius)))
                elif(radius > 80):
                    if self.move.calibration:
                        self.move.reverse()
                    else:
                        print("Reverse -> Dist: " + str(int(offset_dist))+ "Radius: " + str(int(radius)))
                else:
                    if self.move.calibration:
                        self.move.stop()
                    else:
                        print("Stopped -> Radius: " + str(int(radius)))     
            if self.gui:
                #Show the the object in video frame 
                cv2.imshow("Frame", frame)
                key = cv2.waitKey(1) & 0xFF
                # if the 'q' key is pressed, stop the loop
                if key == ord("q"):
	                break


    def showGUI(self):
        self.gui = True
    





        