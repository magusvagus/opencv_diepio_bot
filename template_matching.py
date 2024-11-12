import cv2 as cv
import numpy as np

# thresholding template matching
def thresholding(image, needle ,threshold = 0.35, comp_method=cv.TM_CCOEFF_NORMED):

    result = cv.matchTemplate(image, needle, comp_method)

    # max value location
    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)

    # pentagon needs highier threshold, player character gives false positive.
    # positives is a 2D list of x,y coordinates
    positives = np.where(result >= threshold)

    return positives



# take list of multiple positives and merge into single marks
def mergeMultiplePositives(positives, image, needle, eps = 0.02):

    # fetch image size of the needle
    ySide = needle.shape[0]
    xSide = needle.shape[1]

    # create a list with all rectangles
    rectangles_all = []

    for y, x in zip(positives[0], positives[1]):
        rectangles_all.append( (x, y, x+ySide, y+xSide) )
        rectangles_all.append( (x, y, x+ySide, y+xSide) ) # double list so non-dublicated rectangles dont get lost.

    # group rectangles together near each other -> into new list
    rectangles_grouped, _ = cv.groupRectangles(rectangles_all, 1, eps) # "_" -> ignoring weights value for now

    for rect in rectangles_grouped:
        # (top left), (bottom right) coordinates to draw rectangle
        cv.rectangle(image, (rect[0], rect[1]), (rect[2] , rect[3]), (0,255,0), 2)
        # display dots in the middle of the rectangle to make it clickable for PyAutoGui
        # make the code more readable and simple. Dots could be displayed a little bit lower, but its fine for now.
        cv.circle(image, (int(rect[0]) + int(ySide/2), int(rect[1] + int(xSide/2)) ) , 4, (0,0,255), cv.FILLED)

