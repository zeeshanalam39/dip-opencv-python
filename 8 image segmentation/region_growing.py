# Credits: Dr. Usman Akram

import cv2 as cv
import numpy as np
import math

IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab8\_img.bmp', 0)  # Read Img
cv.imshow('Original Image', IMAGE)
cv.waitKey(0)
cv.destroyAllWindows()


def regionGrowingAlgo(img):
    epsilon = int(input('Enter epsilon: '))     # Prompt epsilon
    print(np.shape(img))
    size = np.shape(img)    # Get img shape
    rows = size[0]
    cols = size[1]
    img = np.pad(img, pad_width=[(1, 1), (1, 1)], mode='constant', constant_values=0)   # Padd zeros
    print(np.shape(img))
    rc = math.floor(rows/2)     # Center of rows-rc
    cc = math.floor(cols/2)     # Center of cols-cc
    rowsIndex = []              #
    colsIndex = []
    rowsIndex.append(rc)
    colsIndex.append(cc)
    for n in range(0, len(rowsIndex), 1):
        print('LENGTH: ', len(rowsIndex), len(colsIndex))
        x = rowsIndex[n]
        y = colsIndex[n]
        currentPxl = img[x][y]
        if abs(currentPxl-img[x-1][y-1]) < epsilon:
            rowsIndex.append(x-1)
            colsIndex.append(y-1)
        if abs(currentPxl - img[x-1][y]) < epsilon:
            rowsIndex.append(x - 1)
            colsIndex.append(y)
        if abs(currentPxl - img[x-1][y+1]) < epsilon:
            rowsIndex.append(x - 1)
            colsIndex.append(y + 1)
        if abs(currentPxl - img[x][y-1]) < epsilon:
            rowsIndex.append(x)
            colsIndex.append(y - 1)
        if abs(currentPxl - img[x][y+1]) < epsilon:
            rowsIndex.append(x)
            colsIndex.append(y + 1)
        if abs(currentPxl - img[x+1][y-1]) < epsilon:
            rowsIndex.append(x + 1)
            colsIndex.append(y - 1)
        if abs(currentPxl - img[x+1][y]) < epsilon:
            rowsIndex.append(x + 1)
            colsIndex.append(y)
        if abs(currentPxl - img[x+1][y+1]) < epsilon:
            rowsIndex.append(x + 1)
            colsIndex.append(y + 1)

    for r in range(rows):
        for c in range(cols):
            img[r][c] = 0

    for r in range(len(rowsIndex)):
        img[rowsIndex[r]][colsIndex[r]] = 255

    cv.imshow('Region Growing', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


regionGrowingAlgo(IMAGE)    # Call function
