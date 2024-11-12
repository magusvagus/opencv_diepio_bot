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


# FPS count start
fps_start = time.time()

# main loop
while run:
    if windowCapture.screenshot is not None:

        image = windowCapture.screenshot

        # image variable needs conversion, otherwise cv.rectangle function throws err.
        # NOTE: need workaround and color are off.
        # HACK: this works for now
        screenshot = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        screenshot = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        positives = thresholding(screenshot, needle_image, 0.35)

        mergeMultiplePositives(positives, screenshot, needle_image, eps=0.02)

        cv.imshow("Screenshot", screenshot)
        key = cv.waitKey(1)
        if key == ord('q'):
            run = False
            windowCapture.stop()
        
        # FPS count stop
        fps_end = ( 1 / (time.time() - fps_start) )
        print(f"FPS: %f" % fps_end)






