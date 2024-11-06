import cv2 as cv
import numpy as np


# basic image matching
# best comparison method yet still to be determined 

# NOTE: image data of farmables and bullets have been retaken and are now the same depth, no conversion needed!
# FIX: same has still to be done for > enemies, player, UI.
screenshot_img = cv.imread('./screenshots_diepio/gameplay_screenshots/Oct30_224501.png', cv.IMREAD_UNCHANGED)
farm_yellow_cube = cv.imread('./screenshots_diepio/farming/farm_cube2.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(screenshot_img, farm_yellow_cube, cv.TM_CCOEFF_NORMED)

# max value location
minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)
print(maxLoc)

#thresh = cv.threshold(result, 0.7, 1.0, cv.THRESH_BINARY)
#print(thresh)

# fetch image size of the needle
farm_x, farm_y, _ = farm_yellow_cube.shape

# draw rectangle around object
cv.rectangle(screenshot_img, maxLoc, (maxLoc[0] + farm_x, maxLoc[1] + farm_y), (0,255,0), 2, 8, 0)

cv.imshow('Result', screenshot_img)
cv.waitKey()


