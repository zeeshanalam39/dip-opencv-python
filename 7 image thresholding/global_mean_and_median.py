import cv2 as cv
import numpy as np
IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab7\_img1.png', 0)
print(IMAGE.shape)


def globalMean(_img):
    size = np.shape(_img)
    rows = size[0]
    cols = size[1]
    meanImg = np.zeros([rows, cols], dtype=np.uint8)
    mean = np.mean(_img)
    for r in range(rows):
        for c in range(cols):
            meanImg[r][c] = 0 if _img[r][c] < mean else 255

    cv.imshow('Global Mean', meanImg)
    cv.waitKey(0)
    cv.destroyAllWindows()


def globalMedian(_img):
    size = np.shape(_img)
    rows = size[0]
    cols = size[1]
    medianImg = np.zeros([rows, cols], dtype=np.uint8)
    median = np.median(_img)
    for r in range(rows):
        for c in range(cols):
            medianImg[r][c] = 0 if _img[r][c] < median else 255

    cv.imshow('Global Median', medianImg)
    cv.waitKey(0)
    cv.destroyAllWindows()


globalMean(IMAGE)
globalMedian(IMAGE)

