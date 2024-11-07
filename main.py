import cv2 as cv
import numpy as np


# basic image matching
# best comparison method yet still to be determined 

# NOTE: image data of farmables and bullets have been retaken and are now the same depth, no conversion needed!
# FIX: same has still to be done for -> enemies, player, UI.
screenshot_img = cv.imread('./screenshots_diepio/gameplay_screenshots/Oct30_224501.png', cv.IMREAD_UNCHANGED)
yellow_cube = cv.imread('./screenshots_diepio/farming/farm_cube2.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(screenshot_img, yellow_cube, cv.TM_CCOEFF_NORMED)

# max value location
minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)

# fetch image size of the needle
y_Cube, x_Cube, _ = yellow_cube.shape

# pentagon needs highier threshold, player character gives false positive.
threshold = 0.35
yLoc, xLoc = np.where(result >= threshold)


# create a list with all rectangles
rectangles_all = []

for y, x in zip(yLoc, xLoc):
    rectangles_all.append( (x, y, x+y_Cube, y+x_Cube) )
    rectangles_all.append( (x, y, x+y_Cube, y+x_Cube) ) # double list so non-dublicated rectangles dont get lost.

# group rectangles together near each other -> into new list
rectangles_grouped, _ = cv.groupRectangles(rectangles_all, 1, 0.02) # "_" -> ignoring weights value

for rect in rectangles_grouped:
    # (top left), (bottom right) coordinates to draw rectangle
    cv.rectangle(screenshot_img, (rect[0], rect[1]), (rect[2] , rect[3]), (0,255,0), 2)

cv.imshow('Result', screenshot_img)
cv.waitKey()








