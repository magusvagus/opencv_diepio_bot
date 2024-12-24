import cv2


def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colors = image[y,x]
        print(f"RGB: {colors} Coordinates: Y/{y}, X{x}")

# Read an image, a window and bind the function to window

# example with leveling tree and levelup
image = cv2.imread("../../../../../screenshots/heute-low.png")
cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)

#image = cv2.resize(image, (960,540))
#image = cv2.resize(image, (1920,1080))

#Do until esc pressed
while(1):
    cv2.imshow('mouseRGB',image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
#if esc pressed, finish.
cv2.destroyAllWindows()
