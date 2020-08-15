import cv2 as cv
import numpy as np

IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab7\_img1.png', 0)
cv.imshow('Original Image', IMAGE)
cv.waitKey()
cv.destroyAllWindows()
print(IMAGE.shape)


def globalAdaptiveThreshold(_img):
    size = np.shape(_img)   # Find img size
    rows = size[0]
    cols = size[1]

    newImg = np.zeros([rows, cols], dtype=np.uint8)    # New img
    group1 = group2 = []                                # Lists to store groups
    prevThreshold = int(np.mean(_img))                  # Initial threshold

    epsilon = 8
    for r in range(0, rows):        # Initial thresholding
        for c in range(0, cols):
            if _img[r][c] < prevThreshold:
                group1.append(_img[r][c])
            else:
                group2.append(_img[r][c])

    m1 = sum(group1)/len(group1)    # Find mean of each group
    m2 = sum(group2)/len(group2)
    nextThreshold = (m1 + m2)/2     # Find new threshold

    while abs(nextThreshold-prevThreshold) >= epsilon:  # Keep going if condition is not satisfied.
        group1 = group2 = []    # Clear groups

        for r in range(0, rows):    # Again threshold
            for c in range(0, cols):
                if _img[r][c] < nextThreshold:
                    group1.append(_img[r][c])
                else:
                    group2.append(_img[r][c])

        prevThreshold = nextThreshold
        m1 = sum(group1) / len(group1)  # Find mean of each group
        m2 = sum(group2) / len(group2)
        nextThreshold = (m1 + m2) / 2

    for r in range(0, rows):    # Thresholding on the basics of final threshold after condition is met.
        for c in range(0, cols):
            newImg[r][c] = 0 if _img[r][c] < nextThreshold else 255

    print(newImg.shape)
    cv.imshow('Global Adaptive Thresholding', newImg)    # Show image
    cv.waitKey(0)
    cv.destroyAllWindows()


globalAdaptiveThreshold(IMAGE)


