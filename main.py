import cv2 as cv
import numpy as np
import time
import sys

import Xlib
import Xlib.XK
import Xlib.display
from Xlib import X
from Xlib.ext.xtest import fake_input

from movement import movement, pushKey
from window_capture import WindowCapture

from ultralytics import YOLO


print("Initializing Program")
# define window/ app to capture
windowCapture = WindowCapture('librewolf')
windowCapture.start()
run = True



# load images
#needle_image = cv.imread('./screenshots_diepio/farming/farm_cube2.png', cv.IMREAD_UNCHANGED)
#image = cv.imread('./screenshots_diepio/gameplay_screenshots/Oct30_224501.png', cv.IMREAD_UNCHANGED)


# create HSV trackbars for masking
#TrackbarsHSV("Trackbars", "LH","LS","LV","UH","US","UV", 0, 255)



print("Loading YOLO model...")
# load YOLO AI image
yolo = YOLO('./runs/detect/yolo_v8n_diep2k2/weights/best.pt')



# Function to get class colors
def getColours(cls_num):
    base_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    color_index = cls_num % len(base_colors)
    increments = [(1, -2, 1), (-2, 1, -1), (1, -1, 2)]
    color = [base_colors[color_index][i] + increments[color_index][i] * 
    (cls_num // len(base_colors)) % 256 for i in range(3)]
    return tuple(color)


# WARN: still to be tested !!!

# if coordinates are equal to set value, do..
def checkPixelVal(root, image, stats, coordinates, colorRGB):

    # move mouse pointer to pixel
    root.warp_pointer(coordinates[0], coordinates[1])

    # check for given RGB value
    # FIX: move to seperate function
    if np.all( image[coordinates[0],coordinates[1]] == [colorRGB[0],colorRGB[1],colorRGB[2]] ):
        # level up skill
        if stats[5] <= 4:
            pushKey('6')
            stats[5] =+ 1

        elif stats[5] == 4:
            pushKey('5')
            stats[4] =+ 1

        elif stats[4] == 4:
            pushKey('7')
            stats[6] =+ 1

        elif stats[6] == 4:
            pushKey('8')
            stats[7] =+ 1

        # elif stats[7] == 3 and stats[5] != 7:
        #     pushKey('6')
        #     stats[5] =+ 1




# 5 sec delay
print(f"program starts in 5 seconds.")
time.sleep(5)



# FPS count start
fps_start = time.time()



# stats levels
health_regen       = 0 # key 1
max_health         = 0 # key 2
body_damage        = 0 # key 3
bullet_speed       = 0 # key 4
bullet_penetration = 0 # key 5
bullet_damage      = 0 # key 6
reload             = 0 # key 7
movement_speed     = 0 # key 8

# current test build -> Octo-tank: 0/2/3/0/7/7/7/7
# Overlord: 0/2/3/7/7/7/0/7

# FIX: move to seperate function
stats = [ 
    health_regen, 
    max_health,
    body_damage,
    bullet_speed,
    bullet_penetration,
    bullet_damage,
    reload,
    movement_speed
    ]

# leveling paths
# Tank -> Twin   -> Quad     -> Octotank
# Tank -> Sniper -> Overseer -> Overlord



# declaring variables for targets
closest_target = None

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
                    x3 = int(x1 + ( (x2-x1)/2) )
                    y3 = int(y1 + ( (y2-y1)/2) )

                    # middle coordinates of the player character
                    pX = int(screenshot.shape[1] / 2)
                    pY = int(screenshot.shape[0] / 2)
                    player_pos = (pX, pY)



                    # get the class
                    cls = int(box.cls[0])

                    # get the class name
                    class_name = classes_names[cls]



                    ## auto-aim at nearest target ##

                    # get distance using Euclidean distance formula
                    distance = ((x3 - pX) **2 + (y3 - pY) **2) **.5

                    if closest_target == None:
                        closest_target =  (x3 , y3)

                    else:
                        # get new distance for comparison
                        compare = ((closest_target[0] - pX) **2 + (closest_target[1] - pY) **2) **.5

                        if distance < compare:
                            closest_target = (x3, y3)

                            # print current target info
                            print(f"Class name: {class_name}\n")
                            print(f"Current target coordinates: {closest_target[0], closest_target[1]}\n")
                            print(f"Distance: {distance}\n")
                            # additional debug info
                            print(f"All boxes: {result.boxes}")



                    # get the respective color
                    colour = getColours(cls)

                    # draw the rectangle
                    cv.rectangle(screenshot, (x1,y1), (x2,y2), colour, 2)

                    # put the class name and confidence on the image
                    cv.putText(screenshot, f'{classes_names[int(box.cls[0])]} {box.conf[0]:.2f}', (x1, y1), cv.FONT_HERSHEY_SIMPLEX, 1, colour, 1)



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

            if window_title_property and window_name.lower() in window_title_property.value.decode('utf-8').lower():
                windowId = windowID


            # move mouse to X, Y position
            if closest_target == None:
                pass
            else:

                # NOTE: for testing (will be removed later)
                pX = int(screenshot.shape[1] / 2)
                pY = int(screenshot.shape[0] / 2)
                distance = ((closest_target[0] - pX) **2 + (closest_target[1] - pY) **2) **.5


                root.warp_pointer(closest_target[0],closest_target[1])

                # press mouse button 1 (shoot)
                fake_input(display, X.ButtonPress, 1)
                fake_input(display, X.ButtonRelease, 1)

                # move to target
                movement(closest_target, (pX, pY))

                # check given pixel for RGB value
                # checkPixelVal(root, screenshot, stats, (249,864), (233,233,233) )

                # reset aim bot
                closest_target = None



    # finnish after a minute if keyboard stops working
    # on DWM restart helps
    if ((time.time() / 60) - (fps_start / 60)) >= 1:
        print("time is over")
        exit()
    else:
        pass



    # show comuter vision on seperate window
    #cv.imshow("Screenshot", screenshot)

    key = cv.waitKey(1)
    if key == ord('q'):
        run = False
        windowCapture.stop()



    # FPS count stop && show
    fps_end = ( 1 / (time.time() - fps_start) )
    print(f"\nFPS: %f\n" % fps_end)






