import Xlib
import Xlib.XK
import Xlib.display
from Xlib import X
from Xlib.ext.xtest import fake_input

# move towards target
# NOTE: HORRIBLE protoype/ proof of concept, needs to be further improved.

def keyboardReset(display, keys = ['Up','Down','Left','Right']):
    # iterate over each given key and release it
    for key in keys:
        keysym = Xlib.XK.string_to_keysym(key)
        keycode = display.keysym_to_keycode(keysym)
        Xlib.ext.xtest.fake_input(display, Xlib.X.KeyRelease, keycode)

    

def movement(display, target ,player):

    # keyboard key push and release example code

    # keysym = Xlib.XK.string_to_keysym('Down')
    # keycode = display.keysym_to_keycode(keysym)
    # Xlib.ext.xtest.fake_input(window, Xlib.X.KeyPress, keycode)
    # Xlib.ext.xtest.fake_input(window, Xlib.X.KeyRelease, keycode)

    # FIX: this seems to prever left right movement, probably due to
    # fact that there is no buffer zone in wich the bot can stop. Its
    # either to big or to low.

    # NOTE: placeholder distance for testing, optimal distance still to be found (assuming the whole function wont be re-written)
    distance = 20

    # trigger event based on distance

    # if target X axis is SMALLER player X axis move towards it
    if target[0] <= (player[0] - distance):

        # reset all previous pushed keys
        keyboardReset(display)

        # push key
        keysym = Xlib.XK.string_to_keysym('Left')
        keycode = display.keysym_to_keycode(keysym)
        Xlib.ext.xtest.fake_input(display, Xlib.X.KeyPress, keycode)

    # if target Y axis is SMALLER player Y axis move towards it
    elif target[1] < (player[1] - distance):

        # reset all previous pushed keys
        keyboardReset(display)

        # push key
        keysym = Xlib.XK.string_to_keysym('Up')
        keycode = display.keysym_to_keycode(keysym)
        Xlib.ext.xtest.fake_input(display, Xlib.X.KeyPress, keycode)

    # if target X axis is BIGGER player X axis move towards it
    elif target[0] > (player[0] + distance):

        # reset all previous pushed keys
        keyboardReset(display)

        # push key
        keysym = Xlib.XK.string_to_keysym('Right')
        keycode = display.keysym_to_keycode(keysym)
        Xlib.ext.xtest.fake_input(display, Xlib.X.KeyPress, keycode)

    # if target Y axis is BIGGER player Y axis move towards it
    elif target[1] > (player[1] + distance):

        # reset all previous pushed keys
        keyboardReset(display)

        # push key
        keysym = Xlib.XK.string_to_keysym('Down')
        keycode = display.keysym_to_keycode(keysym)
        Xlib.ext.xtest.fake_input(display, Xlib.X.KeyPress, keycode)

    elif target == None:

        # reset all previous pushed keys
        keyboardReset(display)

