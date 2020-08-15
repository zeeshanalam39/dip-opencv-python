import cv2 as cv    # Importing opencv package
import numpy as np  # Importing numpy
import math

IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab10\_img3.tif')  # Read coloured img
cv.imshow('Original Image', IMAGE)     # Show img
cv.waitKey()
cv.destroyAllWindows()

red_channel, green_channel, blue_channel = cv.split(IMAGE)  # Getting seperate channels


# Applying Gaussian Filter
def padding(img, padd):     # Add Padding
    img = np.pad(img, pad_width=[(padd, padd), (padd, padd)], mode='constant', constant_values=0)
    return img


def createMask(img):    # Create mask/filter
    m = int(input('Enter mask size m: '))   # Get mask size
    n = int(input('Enter mask size n: '))
    if m != n:
        print('Invalid mask size! Try again :)')
        createMask()
    mask = np.zeros([m, n], dtype=np.int_)
    for i in range(m):
        for j in range(n):
            mask[i][j] = int(input('Enter value for mask index: '))
    mask = mask/(m*n)
    p = math.floor((m-1)/2)     # Find padding size
    return [padding(img, p), mask, p]


def normalize(_img):    # Normalize img
    size = np.shape(_img)
    rows = size[0]
    cols = size[1]
    min = _img.min()
    max = _img.max()
    for r in range(rows):
        for c in range(cols):
            _img[r][c] = ((_img[r][c] - min)/(max - min)) * 255

    return _img


def applyFilter(img):   # Apply filter
    res = createMask(img)
    paddedImg = res[0]
    mask = res[1]
    paddSize = res[2]
    size = np.shape(img)
    rows = size[0]
    cols = size[1]
    size = np.shape(mask)   # Getting shape of filter.
    fr = size[0]
    fc = size[1]
    currentImg = np.zeros([fr, fc])
    for r in range(rows):
        for c in range(cols):
            if r > paddSize-1 and c > paddSize-1:
                currentImg = paddedImg[r-paddSize:r+paddSize+1, c-paddSize:c+paddSize+1]
                paddedImg[r][c] = np.sum(mask * currentImg)

    paddedImg = normalize(paddedImg)
    return paddedImg


# Applying Sobels
def sobel(img):
    sobelX = cv.Sobel(img, cv.CV_8U, 1, 0, ksize=3)    # Calulating sobelX
    sobelY = cv.Sobel(img, cv.CV_8U, 0, 1, ksize=3)    # Calulating sobelY
    size = np.shape(sobelX)
    rows = size[0]
    cols = size[1]
    gradMag = np.zeros([rows, cols])    # Matrix to store sobelXY result.
    
    gradMag = abs(sobelX) + abs(sobelY)
    # for r in range(rows):
    #     for c in range(cols):
    #         gradMag[r][c] = math.sqrt((sobelX[r][c]) ** 2 + (sobelY[r][c] ** 2))

    return gradMag


# Calling function to apply gaussian on R, G, B Channels
red_channel_gaussian = applyFilter(red_channel)
green_channel_gaussian = applyFilter(green_channel)
blue_channel_gaussian = applyFilter(blue_channel)
rgb_gaussian = cv.merge([red_channel_gaussian, green_channel_gaussian, blue_channel_gaussian])  # Combining results
cv.imshow('RGB Gaussian', rgb_gaussian)
cv.waitKey()
cv.destroyAllWindows()

# Calling function to apply SobelX & SobelY on R, G, B Channels
red_channel_sobel = sobel(red_channel)
green_channel_sobel = sobel(green_channel)
blue_channel_sobel = sobel(blue_channel)
rgb_sobel = cv.merge([red_channel_sobel, green_channel_sobel, blue_channel_sobel])
cv.imshow('RGB Sobel', rgb_sobel)
cv.waitKey()
cv.destroyAllWindows()





