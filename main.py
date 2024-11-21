import cv2 as cv
import numpy as np
import time

import Xlib
import Xlib.display
from Xlib import X
from Xlib.ext.xtest import fake_input

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



# 5 sec delay
print(f"program starts in 5 seconds.")
time.sleep(5)



# FPS count start
fps_start = time.time()



# list for targets
targets = []
targets_update = []

cycle = 0
#global closest_target

# main loop
while run:
    if windowCapture.screenshot is not None:

        image = windowCapture.screenshot



        # image variable needs conversion, otherwise cv.rectangle function throws err.
        # NOTE: need workaround and colors are off.
        # HACK: this works for now
        screenshot = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        #screenshot = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        # resize the screenshot
        #screenshot = cv.resize(screenshot, (900,600))

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



                    # middle coordinates of the rectangle
                    x3 = int(x1 + ((x2-x1)/2))
                    y3 = int(y1 + ((y2-y1)/2))

                    # middle coordinates of the player character
                    pX = int(screenshot.shape[1] / 2)
                    pY = int(screenshot.shape[0] / 2)
                    player_pos = (pX, pY)



                    # auto shoot nearest found target
                    # adding a tuple with the x and y sum for sorting
                    # if list gets to big, update list
                    if (len(targets_update) < 42) and (len(targets) < 42):
                        targets_update.append( (x3,y3) )
                        targets.append( (x3,y3) )

                    # fetch closest target to player coordinates
                    closest_target = min(targets, key=lambda y: abs( (y[0]+y[1]) - (player_pos[0]+player_pos[1]) ))

                    if closest_target not in targets_update:
                        targets = targets_update
                        targets_update.clear()
                    elif len(targets_update) > 22:
                        targets_update.clear()



                    # get the class
                    cls = int(box.cls[0])

                    # get the class name
                    class_name = classes_names[cls]

                    # get the respective colour
                    colour = getColours(cls)

                    # draw the rectangle
                    cv.rectangle(screenshot, (x1,y1), (x2,y2), colour, 2)

                    # put the class name and confidence on the image
                    cv.putText(screenshot, f'{classes_names[int(box.cls[0])]} {box.conf[0]:.2f}', (x1, y1), cv.FONT_HERSHEY_SIMPLEX, 1, colour, 2)



                    # click on found target
                    # get window ID
                    # FIX: no need to do that a second time
                    window_name = 'librewolf'
                    display = Xlib.display.Display()
                    root = display.screen().root
                    windowIDs = root.get_full_property(display.intern_atom('_NET_CLIENT_LIST'), X.AnyPropertyType).value

                    for windowID in windowIDs:
                        window = display.create_resource_object('window', windowID)
                        window_title_property = window.get_full_property(display.intern_atom('_NET_WM_NAME'), 0)

                        if window_title_property and window_name.lower() in window_title_property.value.decode('utf-8').lower() and (len(targets) == 42):
                            windowId = windowID


                        # move mouse to X, Y position
                        root.warp_pointer(closest_target[0],closest_target[1])

                        # press mouse button 1 (shoot)
                        fake_input(display, X.ButtonPress, 1)



        # show comuter vision on seperate window
        #cv.imshow("Screenshot", screenshot)

        key = cv.waitKey(1)
        if key == ord('q'):
            run = False
            windowCapture.stop()



        # FPS count stop
        fps_end = ( 1 / (time.time() - fps_start) )
        print(f"FPS: %f" % fps_end)






