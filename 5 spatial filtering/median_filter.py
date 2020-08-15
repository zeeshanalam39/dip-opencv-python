import cv2 as cv
import numpy as np
import math
img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab5\_img3.tif', 0)
print(img.shape)
cv.imshow('Original Image', img)
cv.waitKey(0)
cv.destroyAllWindows()


def padding(imgPadd, padd):     # Function to add zeros
    print('>> Size before padding: ', imgPadd.shape)
    imgPadd = np.pad(imgPadd, pad_width=[(padd, padd), (padd, padd)], mode='constant', constant_values=0)
    print('>> Size after padding: ', imgPadd.shape)
    return imgPadd


def createMask():               # Mask related work
    m = int(input('Enter mask size m: '))
    n = int(input('Enter mask size n: '))
    if m != n:      # Check for valid mask size
        print('Invalid mask size! Try again :(')
        createMask()
    p = math.floor((m-1)/2)     # Find padding size
    return [padding(img, p), p, m]  # Return padding img, padding size & mask size


def applyFilter():
    res = createMask()
    paddedImg = res[0]  # Padded Img
    paddSize = res[1]   # Padding Size
    fr = fc = res[2]    # Filter Size
    i = math.ceil((fr * fc) / 2) - 1
    size = np.shape(img)
    rows = size[0]
    cols = size[1]
    print(rows, cols)
    currentImg = np.zeros([fr, fc])
    for r in range(rows):
        for c in range(cols):
            if r > paddSize-1 and c > paddSize-1:
                currentImg = paddedImg[r-paddSize:r+paddSize+1, c-paddSize:c+paddSize+1]
                paddedImg[r][c] = np.sort(currentImg.flatten())[i]

    cv.imshow('Image', paddedImg)
    cv.waitKey(0)
    cv.destroyAllWindows()


applyFilter()
