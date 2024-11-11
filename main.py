import cv2 as cv
import numpy as np
import time
from window_capture import WindowCapture


windowCapture = WindowCapture('librewolf')
windowCapture.start()
run = True


# FIX: UI image data has to be retaken.
yellow_cube = cv.imread('./screenshots_diepio/farming/farm_cube2.png', cv.IMREAD_UNCHANGED)


# FPS count start
fps_start = time.time()

# main loop
while run:
    if windowCapture.screenshot is not None:
        image = windowCapture.screenshot

        # image variable needs conversion, otherwise cv.rectangle function throws err.
        # NOTE: need workaround and color are off.
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        result = cv.matchTemplate(image, yellow_cube, cv.TM_CCOEFF_NORMED)

        # max value location
        minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)

        # fetch image size of the needle
        y_Cube = yellow_cube.shape[0]
        x_Cube = yellow_cube.shape[1]

        # pentagon needs highier threshold, player character gives false positive.
        threshold = 0.35
        yLoc, xLoc = np.where(result >= threshold)

        # create a list with all rectangles
        rectangles_all = []


        for y, x in zip(yLoc, xLoc):
            rectangles_all.append( (x, y, x+y_Cube, y+x_Cube) )
            rectangles_all.append( (x, y, x+y_Cube, y+x_Cube) ) # double list so non-dublicated rectangles dont get lost.

        # group rectangles together near each other -> into new list
        rectangles_grouped, _ = cv.groupRectangles(rectangles_all, 1, 0.02) # "_" -> ignoring weights value for now


        for rect in rectangles_grouped:
            # (top left), (bottom right) coordinates to draw rectangle
            cv.rectangle(image, (rect[0], rect[1]), (rect[2] , rect[3]), (0,255,0), 2)
            # display dots in the middle of the rectangle to make it clickable for PyAutoGui
            # make the code more readable and simple. Dots could be displayed a little bit lower, but its fine for now.
            cv.circle(image, (int(rect[0]) + int(y_Cube/2), int(rect[1] + int(x_Cube/2)) ) , 4, (0,0,255), cv.FILLED)


        cv.imshow("Screenshot", image)
        key = cv.waitKey(1)
        if key == ord('q'):
            run = False
            windowCapture.stop()
        
        # FPS count stop
        fps_end = ( 1 / (time.time() - fps_start) )
        print(f"FPS: %f" % fps_end)






