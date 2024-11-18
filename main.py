import cv2 as cv
import numpy as np
import time
from ultralytics import YOLO
from window_capture import WindowCapture
from template_matching import *
from hsv_thresholding import *


# define window/ app to capture
windowCapture = WindowCapture('librewolf')
windowCapture.start()
run = True


# load images
#needle_image = cv.imread('./screenshots_diepio/farming/farm_cube2.png', cv.IMREAD_UNCHANGED)
#image = cv.imread('./screenshots_diepio/gameplay_screenshots/Oct30_224501.png', cv.IMREAD_UNCHANGED)


# create HSV trackbars for masking
#TrackbarsHSV("Trackbars", "LH","LS","LV","UH","US","UV", 0, 255)

# load YOLO AI image
yolo = YOLO('./runs/detect/yolo_v8n_diep/weights/best.pt')


# Function to get class colors
def getColours(cls_num):
    base_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    color_index = cls_num % len(base_colors)
    increments = [(1, -2, 1), (-2, 1, -1), (1, -1, 2)]
    color = [base_colors[color_index][i] + increments[color_index][i] * 
    (cls_num // len(base_colors)) % 256 for i in range(3)]
    return tuple(color)


# FPS count start
fps_start = time.time()

# main loop
while run:
    if windowCapture.screenshot is not None:

        image = windowCapture.screenshot

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
        #result, mask, hsv = maskTrackbarsCallback(screenshot,"Trackbars","LH","LS","LV","UH","US","UV")

        # re-convert to rgb from hsv
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2RGB)

        
        # YOLO tracking
        results = yolo.track(screenshot, stream=True)

        for result in results:
        # get the classes names
            classes_names = result.names

        # iterate over each box
            for box in result.boxes:
                # check if confidence is greater than 60 percent
                if box.conf[0] > 0.6:
                    # get coordinates
                    [x1, y1, x2, y2] = box.xyxy[0]
                    # convert to int
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    # get the class
                    cls = int(box.cls[0])

                    # get the class name
                    class_name = classes_names[cls]

                    # get the respective colour
                    colour = getColours(cls)

                    # draw the rectangle
                    cv.rectangle(screenshot, (x1, y1), (x2, y2), colour, 2)

                    # put the class name and confidence on the image
                    cv.putText(screenshot, f'{classes_names[int(box.cls[0])]} {box.conf[0]:.2f}', (x1, y1), cv.FONT_HERSHEY_SIMPLEX, 1, colour, 2)


        cv.imshow("Screenshot", screenshot)
        # cv.imshow("hsv", hsv)
        # cv.imshow("mask", mask)
        # cv.imshow("result", result)

        key = cv.waitKey(1)
        if key == ord('q'):
            run = False
            windowCapture.stop()



        # FPS count stop
        fps_end = ( 1 / (time.time() - fps_start) )
        print(f"FPS: %f" % fps_end)






