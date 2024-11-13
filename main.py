import cv2 as cv
import numpy as np
import time
from window_capture import WindowCapture
from template_matching import thresholding, mergeMultiplePositives






# define window/ app to capture
windowCapture = WindowCapture('librewolf')
windowCapture.start()
run = True

# load needle image
needle_image = cv.imread('./screenshots_diepio/farming/farm_cube2.png', cv.IMREAD_UNCHANGED)
image = cv.imread('./screenshots_diepio/gameplay_screenshots/Oct30_224501.png', cv.IMREAD_UNCHANGED)


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

    mask = cv.inRange(hsv, lower, upper)

    # apply the mask to the frame
    result = cv.bitwise_and(screenshot, screenshot, mask=mask)

    return result, mask, hsv

# create HSV trackbars for masking
TrackbarsHSV("Trackbars", "LH","LS","LV","UH","US","UV", 0, 255)

# FPS count start
fps_start = time.time()

# main loop
while run:
    if windowCapture.screenshot is not None:

        #image = windowCapture.screenshot

        # image variable needs conversion, otherwise cv.rectangle function throws err.
        # NOTE: need workaround and color are off.
        # HACK: this works for now
        screenshot = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        #screenshot = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        #positives = thresholding(screenshot, needle_image, 0.35)
        #mergeMultiplePositives(positives, screenshot, needle_image, eps=0.02)

        # resize the screenshot
        screenshot = cv.resize(screenshot, (900,600))

        # trackbars callback function
        result, mask, hsv = maskTrackbarsCallback(screenshot,"Trackbars","LH","LS","LV","UH","US","UV")


        cv.imshow("Screenshot", screenshot)
        cv.imshow("hsv", hsv)
        cv.imshow("mask", mask)
        cv.imshow("result", result)

        key = cv.waitKey(1)
        if key == ord('q'):
            run = False
            windowCapture.stop()



        # FPS count stop
        fps_end = ( 1 / (time.time() - fps_start) )
        print(f"FPS: %f" % fps_end)






