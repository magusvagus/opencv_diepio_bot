from pynput.keyboard import Key, Controller

# move towards target

# NOTE: HORRIBLE protoype/ proof of concept, needs to be further improved.

# NOTE: Xlib library has been scraped, and replaced with pynput due to more consistant/ predictable results. Future versions will need to go back to Xlib preferbly XCB



# WARN: functions still to be tested!!!
def releaseArrowKeys(keys=[Key.down, Key.up, Key.left, Key.right]):
    keyboard = Controller()

    for key in keys:
        # reset previous pushed keys
        keyboard.release(key)


# push and release key X times
def pushKey(key, repeat=1):

    for i in range(repeat):
        keyboard = Controller()
        keyboard.press(key)




def movement(target ,player):

    # FIX: this seems to prever left right movement, probably due to
    # fact that there is no buffer zone in wich the bot can stop. Its
    # either to big or to low.

    # NOTE: placeholder distance for testing, optimal distance still to be found (assuming the whole function wont be re-written)
    # distance in pixels
    distance = 160

    # trigger event based on distance

    # if target X axis is SMALLER player X axis move towards it
    if target[0] <= (player[0] - distance):

        # reset previous pushed arrow keys
        releaseArrowKeys()

        # push and realese key
        pushKey(Key.left, 1)

    # if target Y axis is SMALLER player Y axis move towards it
    elif target[1] <= (player[1] - distance):

        # reset previous pushed arrow keys
        releaseArrowKeys()

        # push and realese key
        pushKey(Key.up, 1)


    # if target X axis is BIGGER player X axis move towards it
    elif target[0] >= (player[0] + distance):

        # reset previous pushed arrow keys
        releaseArrowKeys()

        # push and realese key
        pushKey(Key.right, 1)


    # if target Y axis is BIGGER player Y axis move towards it
    elif target[1] >= (player[1] + distance):

        # reset previous pushed arrow keys
        releaseArrowKeys()

        # push and realese key
        pushKey(Key.down, 1)


    else:
        # reset all previous pushed keys
        releaseArrowKeys()

    # if this is added the tank move very very slow this might be
    # useful
    # keyboard = Controller()
    # keyboard.release(Key.down)
    # keyboard.release(Key.up)
    # keyboard.release(Key.left)
    # keyboard.release(Key.right)
