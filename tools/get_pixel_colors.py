import cv2


def RGBhigh(image):

    # health regen
    print("//HEALTH REGEN")
    print(f"Level1: {image[886,45]}")
    print(f"Level2: {image[886,70]}")
    print(f"Level3: {image[886,94]}")
    print(f"Level4: {image[886,117]}")
    print(f"Level5: {image[886,132]}")
    print(f"Level6: {image[886,164]}")
    print(f"Level7: {image[886,186]}\n")

    # max health
    print("//MAX REGEN")
    print(f"Level1: {image[910,46]}")
    print(f"Level2: {image[910,70]}")
    print(f"Level3: {image[910,94]}")
    print(f"Level4: {image[910,117]}")
    print(f"Level5: {image[910,132]}")
    print(f"Level6: {image[910,164]}")
    print(f"Level7: {image[910,186]}\n")

    # body damage
    print("//BODY DAMAGE")
    print(f"Level1: {image[932,46]}")
    print(f"Level2: {image[932,70]}")
    print(f"Level3: {image[932,94]}")
    print(f"Level4: {image[932,117]}")
    print(f"Level5: {image[932,132]}")
    print(f"Level6: {image[932,164]}")
    print(f"Level7: {image[932,186]}\n")

    # bullet speed
    print("//BULLET DAMAGE")
    print(f"Level1: {image[956,45]}")
    print(f"Level2: {image[956,71]}")
    print(f"Level3: {image[956,94]}")
    print(f"Level4: {image[956,117]}")
    print(f"Level5: {image[956,140]}")
    print(f"Level6: {image[956,164]}")
    print(f"Level7: {image[956,186]}\n")



def RGBlow(image):

    # bullet penetration
    print("//BULLET PENETRATION")
    print(f"Level1: {image[978,46]}")
    print(f"Level2: {image[978,73]}")
    print(f"Level3: {image[978,95]}")
    print(f"Level4: {image[979,118]}")
    print(f"Level5: {image[979,140]}")
    print(f"Level6: {image[979,165]}")
    print(f"Level7: {image[979,186]}\n")

    # bullet damage
    print("//BULLET DAMAGE")
    print(f"Level1: {image[996,45]}")
    print(f"Level2: {image[1002,71]}")
    print(f"Level3: {image[1001,94]}")
    print(f"Level4: {image[1001,114]}")
    print(f"Level5: {image[1001,141]}")
    print(f"Level6: {image[1001,165]}")
    print(f"Level7: {image[1002,188]}\n")

    # reload
    print("//RELOAD")
    print(f"Level1: {image[1025,44]}")
    print(f"Level2: {image[1025,70]}")
    print(f"Level3: {image[1025,94]}")
    print(f"Level4: {image[1025,117]}")
    print(f"Level5: {image[1025,141]}")
    print(f"Level6: {image[1025,163]}")
    print(f"Level7: {image[1025,189]}\n")

    # movement speed
    print("//MOVEMENT SPEED")
    print(f"Level1: {image[1048,44]}")
    print(f"Level2: {image[1048,70]}")
    print(f"Level3: {image[1048,94]}")
    print(f"Level4: {image[1048,117]}")
    print(f"Level5: {image[1048,137]}")
    print(f"Level6: {image[1048,163]}")
    print(f"Level7: {image[1048,189]}\n")


image = cv2.imread("../../../../../screenshots/heute-high.png")
RGBhigh(image)


image2 = cv2.imread("../../../../../screenshots/heute-low.png")
RGBlow(image2)

#cv2.namedWindow('mouseRGB')

#image = cv2.resize(image, (1920,1080))


#Do until esc pressed
# while(1):
#     cv2.imshow('mouseRGB',image)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
# #if esc pressed, finish.
cv2.destroyAllWindows()

'''
//HEALTH REGEN
Level1: [143 182 237]
Level2: [143 182 237]
Level3: [143 182 237]
Level4: [143 182 237]
Level5: [143 182 237]
Level6: [143 182 237]
Level7: [143 182 237]

//MAX REGEN
Level1: [217 101 213]
Level2: [217 101 213]
Level3: [217 101 213]
Level4: [217 101 213]
Level5: [217 101 213]
Level6: [217 101 213]
Level7: [217 101 213]

//BODY DAMAGE
Level1: [239 107 154]
Level2: [239 107 154]
Level3: [239 107 154]
Level4: [239 107 154]
Level5: [239 107 154]
Level6: [239 107 154]
Level7: [239 107 154]

//BULLET DAMAGE
Level1: [237 147 105]
Level2: [237 147 105]
Level3: [237 147 105]
Level4: [237 147 105]
Level5: [237 147 105]
Level6: [237 147 105]
Level7: [237 147 105]

//BULLET PENETRATION
Level1: [101 210 233]
Level2: [101 210 233]
Level3: [101 210 233]
Level4: [101 210 233]
Level5: [101 210 233]
Level6: [101 210 233]
Level7: [101 210 233]

//BULLET DAMAGE
Level1: [101 101 233]
Level2: [ 97  97 218]
Level3: [101 101 233]
Level4: [101 101 233]
Level5: [101 101 233]
Level6: [101 101 233]
Level7: [ 97  97 218]

//RELOAD
Level1: [101 233 145]
Level2: [101 233 145]
Level3: [101 233 145]
Level4: [101 233 145]
Level5: [101 233 145]
Level6: [101 233 145]
Level7: [101 233 145]

//MOVEMENT SPEED
Level1: [229 233 101]
Level2: [229 233 101]
Level3: [229 233 101]
Level4: [229 233 101]
Level5: [229 233 101]
Level6: [229 233 101]
Level7: [229 233 101]

//LEVEL UP X
RGB: [233 233 233] Coordinates: Y/864, X249
'''
