import cv2
import numpy as np


def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = image[y,x,0]
        colorsG = image[y,x,1]
        colorsR = image[y,x,2]
        colors = image[y,x]
        print("Red: ",colorsR)
        print("Green: ",colorsG)
        print("Blue: ",colorsB)
        print("BRG Format: ",colors)
        print("Coordinates of pixel: X: ",x,"Y: ",y)

# Read an image, a window and bind the function to window

# example with leveling tree and levelup
image = cv2.imread("../yolo/images/train/screenshotOpenCV232202.png")

cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)

#image = cv2.resize(image, (960,540))
image = cv2.resize(image, (1920,1080))

#Do until esc pressed
while(1):
    cv2.imshow('mouseRGB',image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
#if esc pressed, finish.
cv2.destroyAllWindows()
