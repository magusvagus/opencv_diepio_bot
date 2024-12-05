from pynput.keyboard import Key, Controller

# move towards target

# NOTE: Xlib library has been scraped, and replaced with pynput due to more consistant/ predictable results. Future versions will need to go back to Xlib preferbly XCB, for performance reasons.



# go over each arrow key and release it
def releaseArrowKeys(keys=[Key.down, Key.up, Key.left, Key.right]):

    keyboard = Controller()

    for key in keys:
        # reset previous pushed keys
        keyboard.release(key)



# push and release key X times
def pushKey(key, repeat=1):

    keyboard = Controller()

    for i in range(repeat):
        # removing keyboard = C.. makes the player move faster
        keyboard.press(key)



def movement(target ,player):

    # distance in pixels
    distance = 160

    # trigger event based on distance

    # if target X axis is SMALLER player X axis move towards it
    if target[0] <= (player[0] - distance):
        # reset previous pushed arrow keys
        releaseArrowKeys()

        # push key X times
        pushKey(Key.left, 1)

    # if target Y axis is SMALLER player Y axis move towards it
    elif target[1] <= (player[1] - distance):
        # reset previous pushed arrow keys
        releaseArrowKeys()

        # push key X times
        pushKey(Key.up, 1)

    # if target X axis is BIGGER player X axis move towards it
    elif target[0] >= (player[0] + distance):
        # reset previous pushed arrow keys
        releaseArrowKeys()

        # push key X times
        pushKey(Key.right, 1)

    # if target Y axis is BIGGER player Y axis move towards it
    elif target[1] >= (player[1] + distance):
        # reset previous pushed arrow keys
        releaseArrowKeys()

        # push key X times
        pushKey(Key.down, 1)

    else:
        # reset all previous pushed keys
        releaseArrowKeys()

