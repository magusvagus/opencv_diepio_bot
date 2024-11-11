import numpy as np
from threading import Thread, Lock
import Xlib
import Xlib.display
from Xlib import X

# NOTE: try not to use OOP, lets dumb it down to functions. XCB might be a more wise option for the future (lower level -> faster).
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
