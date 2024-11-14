import cv2 as cv
import numpy as np
import time
import Xlib
import Xlib.display
from Xlib import X


# get window ID from seached window name
def getWindowName(window_name):
    display = Xlib.display.Display()
    try:
        root = display.screen().root
        windowIDs = root.get_full_property(display.intern_atom('_NET_CLIENT_LIST'), X.AnyPropertyType).value

        for windowID in windowIDs:
            window = display.create_resource_object('window', windowID)
            window_title_property = window.get_full_property(display.intern_atom('_NET_WM_NAME'), 0)

            if window_title_property and window_name.lower() in window_title_property.value.decode('utf-8').lower():
                windowId = windowID

                return windowId

        if not windowId:
            raise Exception('Window not found: {}'.format(window_name))
    finally:
        display.close()

# make screenshot based on window ID
def getScreenshot(windowId):
    display = Xlib.display.Display()
    window = display.create_resource_object('window', windowId)

    geometry = window.get_geometry()
    width, height = geometry.width, geometry.height

    pixmap = window.get_image(0, 0, width, height, X.ZPixmap, 0xffffffff)
    data = pixmap.data
    image = np.frombuffer(data, dtype='uint8').reshape((height, width, 4))

    return image




# capture window called "librewolf"
windowname = getWindowName("librewolf")
print(windowname)
image = getScreenshot(windowname)


# print out current time H:M:S to be used in screenshot file name
n = time.time()
time_format = time.strftime("%H%M%S", time.gmtime(n))
time = int(time_format) + 10000

# set filename for screenshot
fileName = f"screenshotOpenCV{time}.png"

# show taken screenshot
cv.imshow("result", image)
cv.waitKey()

#cv.imwrite(fileName, image)
