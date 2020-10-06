import cv2
import numpy as np
import configparser

def nothing(x):
    pass

vs = cv2.VideoCapture(0)
# Create a window for options
cv2.namedWindow("HSV Color Selection")
cv2.createTrackbar("LH", "HSV Color Selection", 0, 255, nothing)
cv2.createTrackbar("LS", "HSV Color Selection", 0, 255, nothing)
cv2.createTrackbar("LV", "HSV Color Selection", 0, 255, nothing)
cv2.createTrackbar("UH", "HSV Color Selection", 255, 255, nothing)
cv2.createTrackbar("US", "HSV Color Selection", 255, 255, nothing)
cv2.createTrackbar("UV", "HSV Color Selection", 255, 255, nothing)

while True:
    # get frame
    _, frame = vs.read()
    # convert image to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # get Values from the Trackbar
    l_h = cv2.getTrackbarPos("LH", "HSV Color Selection")
    l_s = cv2.getTrackbarPos("LS", "HSV Color Selection")
    l_v = cv2.getTrackbarPos("LV", "HSV Color Selection")

    u_h = cv2.getTrackbarPos("UH", "HSV Color Selection")
    u_s = cv2.getTrackbarPos("US", "HSV Color Selection")
    u_v = cv2.getTrackbarPos("UV", "HSV Color Selection")

    # create the array with them
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    # mask
    mask = cv2.inRange(hsv, l_b, u_b)

    img = cv2.bitwise_and(frame, frame, mask=mask)

    # cv2.imshow("frame", frame)
    # cv2.imshow("mask", mask)
    cv2.imshow("HSV Color Selection", img)

    key = cv2.waitKey(1) & 0xFF
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
	    break

vs.release()
cv2.destroyAllWindows()