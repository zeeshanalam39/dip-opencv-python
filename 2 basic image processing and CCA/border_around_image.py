import cv2 as cv
import math
import numpy as np
img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab2\Picture5.png', 0)
height, width = img.shape
borderWidth = math.ceil(0.1 * width)
totalWidth = width + (2 * borderWidth)
totalHeight = totalWidth
borderHeight = math.ceil((totalHeight-height)/2)
newImg = np.pad(img, pad_width=[(borderHeight, borderHeight), (borderWidth, borderWidth)], mode='constant', constant_values=255)
cv.imshow('New Image', newImg)
cv.waitKey(50000)
