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


# trackbars

# dummy function
def nothing(x):
    pass

cv.namedWindow("Trackbars")

# indidividual trackbars with upper/ lower HSV values in the
# "Trackbars" window.
cv.createTrackbar("L-H","Trackbars",0,255,nothing)
cv.createTrackbar("L-S","Trackbars",0,255,nothing)
cv.createTrackbar("L-V","Trackbars",0,255,nothing)
cv.createTrackbar("U-H","Trackbars",0,255,nothing)
cv.createTrackbar("U-S","Trackbars",0,255,nothing)
cv.createTrackbar("U-V","Trackbars",0,255,nothing)


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

        # BGR -> Hue Saturation Value
        hsv = cv.cvtColor(screenshot, cv.COLOR_BGR2HSV)


        # connecting the input of the trackbars to the
        # to the inside the main loop
        l_h = cv.getTrackbarPos("L-H","Trackbars")
        l_s = cv.getTrackbarPos("L-S","Trackbars")
        l_v = cv.getTrackbarPos("L-V","Trackbars")
        u_h = cv.getTrackbarPos("U-H","Trackbars")
        u_s = cv.getTrackbarPos("U-S","Trackbars")
        u_v = cv.getTrackbarPos("U-V","Trackbars")

        # taking the Track bar output to the lower variable
        lower = np.array([l_h,l_s,l_v])
        # values we want to detect
        upper = np.array([u_h,u_s,u_v])
        # upper and lower are the bounds any value between
        # those rnges will be detected as white
        mask = cv.inRange(hsv, lower, upper)


        # apply the mask to the frame
        result = cv.bitwise_and(screenshot, screenshot, mask=mask)


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






