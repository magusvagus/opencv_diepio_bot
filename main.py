import cv2 as cv
import numpy as np
import time
from window_capture import WindowCapture
from template_matching import *
from hsv_thresholding import *


# define window/ app to capture
windowCapture = WindowCapture('librewolf')
windowCapture.start()
run = True


# load images
needle_image = cv.imread('./screenshots_diepio/farming/farm_cube2.png', cv.IMREAD_UNCHANGED)
image = cv.imread('./screenshots_diepio/gameplay_screenshots/Oct30_224501.png', cv.IMREAD_UNCHANGED)


# create HSV trackbars for masking
TrackbarsHSV("Trackbars", "LH","LS","LV","UH","US","UV", 0, 255)


# FPS count start
fps_start = time.time()

# main loop
while run:
    if windowCapture.screenshot is not None:

        #image = windowCapture.screenshot

        # image variable needs conversion, otherwise cv.rectangle function throws err.
        # NOTE: need workaround and colors are off.
        # HACK: this works for now
        screenshot = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        #screenshot = cv.cvtColor(image, cv.COLOR_BGR2RGB)


        # NOTE: left for testing purposes
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






