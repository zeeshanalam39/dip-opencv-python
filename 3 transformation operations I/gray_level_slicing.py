import cv2 as cv
import numpy as np

img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab3\es.tif', 0)  # Read image
[w, h] = img.shape                                  # Read image size
for i in range(0, w):                               # Traverse pixels
    for j in range(0, h):
        if img[i][j] < 100 and img[i][j] > 200:     # Check for range
            img[i][j] = 210                         # Change Pixels
cv.imshow('Image', img)                             # Show image
cv.waitKey(50000)
