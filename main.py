import cv2 as cv
import numpy as np


# basic image matching
# best comparison method yet still to be determined 
# no conversion

screenshot_img = cv.imread('./screenshots_diepio/gameplay_screenshots/Oct30_224501.png', cv.IMREAD_UNCHANGED)
screenshot_img = cv.cvtColor(screenshot_img, cv.COLOR_BGR2GRAY) 

#NOTE: images have to be converted to the same depth 
#(a workaround is needed, since this can significantly slow down image processing)

farm_yellow_cube = cv.imread('./screenshots_diepio/farming/yellow_cube1.png', cv.IMREAD_UNCHANGED)
farm_yellow_cube = cv.cvtColor(farm_yellow_cube, cv.COLOR_BGR2GRAY)

result = cv.matchTemplate(screenshot_img, farm_yellow_cube, cv.TM_CCOEFF_NORMED)

cv.imshow('Result', result)
cv.waitKey()


