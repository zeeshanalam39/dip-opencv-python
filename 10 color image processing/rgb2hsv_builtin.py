import cv2 as cv    # Importing opencv package
import numpy as np  # Importing numpy
import math

IMAGE1 = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab10\_img1.tif')  # Read coloured img
cv.imshow('Original Image', IMAGE1)     # Show img
cv.waitKey()
cv.destroyAllWindows()

# IMAGE1 = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab10\_img2.tif')  # Read coloured img
# cv.imshow('Original Image', IMAGE1)  # Show img
# cv.waitKey()
# cv.destroyAllWindows()

hsv = cv.cvtColor(IMAGE1, cv.COLOR_RGB2HSV)     # Get HSV img

cv.imshow('HSV(Builtin Function)', hsv)
cv.waitKey()
cv.destroyAllWindows()





