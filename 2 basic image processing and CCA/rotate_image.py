import cv2 as cv
import numpy as np
from scipy import ndimage

img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab2\Picture5.png', 0)
deg = float(input('Enter degrees: '))
rotated = ndimage.rotate(img, deg)
cv.imshow('Rotated image', rotated)
cv.imwrite('Rotated.png', rotated)
cv.waitKey(50000)