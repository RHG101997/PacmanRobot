# import the necessary packages
from imutils.video import VideoStream
# from move import Move
import numpy as np
import cv2
import imutils
import time
import math



#upper and lower bounds of HSV color space
# orange=>
greenLower = (0, 154, 156)
greenUpper = (255, 255, 255)
camera_horizontal_view = 54


# Will stream video to cv2
vs = VideoStream(0).start()
# vs = VideoStream(src=0).start()
# move = Move()

# Time for Initialization of camera
time.sleep(1.0)

while True:
    # get current frame
    frame = vs.read()
    # If no frame then break out loop
    if frame is None:
	    break
    # Resize for more speed
    # frame = imutils.resize(frame,width=600)
    frame = cv2.resize(frame, (600,480))
    #Blur image for less noice
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	# converting it to color space HSV
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # create a mask of black and white
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    # eroding and dilatation(helps remove smaller blob found in frame)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Getting countor
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
    # make sure the information is from correct version
    cnts = imutils.grab_contours(cnts)
    # Creating center
    center = None


    # if found at least 1 contour
    if len(cnts) > 0:
        # Get the largest contour in mask
        c = max(cnts, key=cv2.contourArea)
        # x,y and radius
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        # Calculate the center of a blob
        # M = cv2.moments(c)
        # using formula x=M10/M00 y=M01/M00  (now we have center)
        # center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])) 

        if radius > 5:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
            # print("The center X:" + str(int(x))+ " Y: " + str(int(y)) + " Radius: " + str(int(radius)))
            cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)

            # Line center of the cam
            # cv2.line(frame, (300,0),(300,480),(0, 255, 255),2)

            #Line from center of screen to center object
            frameCenter = (int(600/2),int(480/2))
            # Get distance from center
            dist = int(x)-frameCenter[0]
            # print("Distance: "+ str(dist))
            # getting to move car
            angle = (abs(dist)*(camera_horizontal_view/2))/300

            cv2.line(frame, (int(x), frameCenter[1]),frameCenter,(0, 0, 255),2)
            if(dist < -100):
                # print("Right -> Dist: " + str(int(dist)) + "Radius: " + str(int(radius)))
                print("Right -> Dist: " + str(int(dist)) + "Angle: " + str(angle))
            elif(dist > 100):
                # print("Left -> Dist: " + str(int(dist))+ "Radius: " + str(int(radius)))
                print("Left -> Dist: " + str(int(dist)) + "Angle: " + str(angle))
            elif(radius < 60):
                print("Forward -> Dist: " + str(int(dist))+ "Radius: " + str(int(radius)))
            else:
                # print("Stopped -> Radius: " + str(int(radius)))
                print("Stopped -> Dist: " + str(int(dist)) + "Angle: " + str(angle))


    
    #Show the the object in video frame 
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
	# if the 'q' key is pressed, stop the loop
    if key == ord("q"):
	    break



# vs.release()
# cv2.destroyAllWindows()



    
