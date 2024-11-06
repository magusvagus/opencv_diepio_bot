import cv2 as cv
import numpy as np


# basic image matching
# best comparison method yet still to be determined 

# NOTE: image data of farmables and bullets have been retaken and are now the same depth, no conversion needed!
# FIX: same has still to be done for > enemies, player, UI.
screenshot_img = cv.imread('./screenshots_diepio/gameplay_screenshots/Oct30_224501.png', cv.IMREAD_UNCHANGED)
yellow_cube = cv.imread('./screenshots_diepio/farming/farm_cube2.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(screenshot_img, yellow_cube, cv.TM_CCOEFF_NORMED)

# max value location
minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)

# fetch image size of the needle
y_Cube, x_Cube, _ = yellow_cube.shape

# draw rectangle around object

# pentagon needs highier threshold, player character gives false positive.
threshold = 0.45
yLoc, xLoc = np.where(result >= threshold)

for i, j in zip(yLoc, xLoc):
    cv.rectangle(screenshot_img, (j, i), (j + y_Cube, i + x_Cube), (0,255,0), 2)

cv.imshow('Result', screenshot_img)
cv.waitKey()


