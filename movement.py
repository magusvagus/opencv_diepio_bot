import Xlib
import Xlib.XK
import Xlib.display
from Xlib import X
from Xlib.ext.xtest import fake_input
from pynput.keyboard import Key, Controller

# move towards target
# NOTE: HORRIBLE protoype/ proof of concept, needs to be further improved.



# WARN: still to be tested!!!

# move into oppsite direction to stop movement
def keyPush(key, repeat=1):

    keyboard = Controller()

    keyboard.press(key)
    keyboard.release(key)




def movement(target ,player):

    # keyboard key push and release example code

    # keysym = Xlib.XK.string_to_keysym('Down')
    # keycode = display.keysym_to_keycode(keysym)
    # Xlib.ext.xtest.fake_input(window, Xlib.X.KeyPress, keycode)
    # Xlib.ext.xtest.fake_input(window, Xlib.X.KeyRelease, keycode)

    # FIX: this seems to prever left right movement, probably due to
    # fact that there is no buffer zone in wich the bot can stop. Its
    # either to big or to low.

    # NOTE: placeholder distance for testing, optimal distance still to be found (assuming the whole function wont be re-written)
    # distance in pixels
    distance = 80

    # trigger event based on distance

    # if target X axis is SMALLER player X axis move towards it
    if target[0] <= (player[0] - distance):
        keyboard = Controller()
        keyboard.release(Key.down)
        keyboard.release(Key.up)
        keyboard.release(Key.left)
        keyboard.release(Key.right)

        keyboard.press(Key.left)
        keyboard.press(Key.left)

    # if target Y axis is SMALLER player Y axis move towards it
    elif target[1] <= (player[1] - distance):
        keyboard = Controller()
        keyboard.release(Key.down)
        keyboard.release(Key.up)
        keyboard.release(Key.left)
        keyboard.release(Key.right)

        keyboard.press(Key.up)
        keyboard.press(Key.up)


    # if target X axis is BIGGER player X axis move towards it
    elif target[0] >= (player[0] + distance):
        keyboard = Controller()
        keyboard.release(Key.down)
        keyboard.release(Key.up)
        keyboard.release(Key.left)
        keyboard.release(Key.right)

        keyboard.press(Key.right)
        keyboard.press(Key.right)


    # if target Y axis is BIGGER player Y axis move towards it
    elif target[1] >= (player[1] + distance):
        keyboard = Controller()

        keyboard.release(Key.down)
        keyboard.release(Key.up)
        keyboard.release(Key.left)
        keyboard.release(Key.right)

        keyboard.press(Key.down)
        keyboard.press(Key.down)


    else:

        keyboard = Controller()
        # reset all previous pushed keys
        keyboard.release(Key.down)
        keyboard.release(Key.up)
        keyboard.release(Key.left)
        keyboard.release(Key.right)

    # if this is added the tank move very slow and steady
    # keyboard = Controller()
    # keyboard.release(Key.down)
    # keyboard.release(Key.up)
    # keyboard.release(Key.left)
    # keyboard.release(Key.right)
