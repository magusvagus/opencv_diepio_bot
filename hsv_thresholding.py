import cv2 as cv
import numpy as np


# create trackbars
def TrackbarsHSV(windowName, LH, LS, LV, UH, US, UV, steps, maxVal):

    # dummy_function
    def dummyFunction(x):
        pass

    cv.namedWindow(windowName)

    # indidividual trackbars with upper/ lower HSV values in the
    # "Trackbars" window.
    cv.createTrackbar(LH,windowName,steps,maxVal,dummyFunction)
    cv.createTrackbar(LS,windowName,steps,maxVal,dummyFunction)
    cv.createTrackbar(LV,windowName,steps,maxVal,dummyFunction)
    cv.createTrackbar(UH,windowName,steps,maxVal,dummyFunction)
    cv.createTrackbar(US,windowName,steps,maxVal,dummyFunction)
    cv.createTrackbar(UV,windowName,steps,maxVal,dummyFunction)


# Callback function trackbars with masking
def maskTrackbarsCallback(screenshot ,windowName, LH, LS, LV, UH, US, UV):

    # BGR -> Hue Saturation Value
    hsv = cv.cvtColor(screenshot, cv.COLOR_BGR2HSV)


    # connecting the input of the trackbars to the
    # to the inside the main loop
    l_h = cv.getTrackbarPos(LH,windowName)
    l_s = cv.getTrackbarPos(LS,windowName)
    l_v = cv.getTrackbarPos(LV,windowName)
    u_h = cv.getTrackbarPos(UH,windowName)
    u_s = cv.getTrackbarPos(US,windowName)
    u_v = cv.getTrackbarPos(UV,windowName)

    # taking the Track bar output to the lower variable
    lower = np.array([l_h,l_s,l_v])
    # values we want to detect
    upper = np.array([u_h,u_s,u_v])
    # upper and lower are the bounds any value between
    # those rnges will be detected as white

    # apply the mask to the frame
    mask = cv.inRange(hsv, lower, upper)
    result = cv.bitwise_and(screenshot, screenshot, mask=mask)

    return result, mask, hsv



























