import cv2 as cv
import numpy as np
from threading import Thread, Lock
import Xlib
import Xlib.display
from Xlib import X

# NOTE: try not to use OOP, lets dumb it down to functions.
class WindowCapture:
    stopped = True
    lock = None
    screenshot = None
    windowId = None

    def __init__(self, window_name):
        self.lock = Lock()
        self.screenshot = None 
        display = Xlib.display.Display()
        try:
            root = display.screen().root
            windowIDs = root.get_full_property(display.intern_atom('_NET_CLIENT_LIST'), X.AnyPropertyType).value

            for windowID in windowIDs:
                window = display.create_resource_object('window', windowID)
                window_title_property = window.get_full_property(display.intern_atom('_NET_WM_NAME'), 0)

                if window_title_property and window_name.lower() in window_title_property.value.decode('utf-8').lower():
                    self.windowId = windowID

            if not self.windowId:
                raise Exception('Window not found: {}'.format(window_name))
        finally:
            display.close()

    def get_screenshot(self):
        display = Xlib.display.Display()
        window = display.create_resource_object('window', self.windowId)

        geometry = window.get_geometry()
        width, height = geometry.width, geometry.height

        pixmap = window.get_image(0, 0, width, height, X.ZPixmap, 0xffffffff)
        data = pixmap.data
        image = np.frombuffer(data, dtype='uint8').reshape((height, width, 4))
        display.close()
        return image

    # threading methods
    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        while not self.stopped:
            # get an updated image of the game
            screenshot = self.get_screenshot()
            # lock the thread while updating the results
            self.lock.acquire()
            self.screenshot = screenshot
            self.lock.release()



windowCapture = WindowCapture('librewolf')
windowCapture.start()
run = True


# FIX: UI image data has to be retaken.
yellow_cube = cv.imread('./screenshots_diepio/farming/farm_cube2.png', cv.IMREAD_UNCHANGED)

# main loop
while run:
    if windowCapture.screenshot is not None:
        image = windowCapture.screenshot

        # image variable needs conversion, otherwise cv.rectangle function throws err.
        # NOTE: need workaround
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

# FIX: this is getting cluttered, seperate into more files and pack some code into functions.

