import cv2 as cv
import numpy as np

img1 = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab3\es.tif', 0) # Read images
img2 = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab3\es.tif', 0)
img3 = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab3\es.tif', 0)
[w, h] = img1.shape             # Find image size
mean1 = np.mean(img1)           # Find image mean
mean2 = np.mean(img2)
mean3 = np.mean(img3)

for i in range(0, w):           # Traverse pixels
    for j in range(0, h):
        # Part a
        if img1[i][j] < mean1:  # Check for condition
            img1[i][j] = 0      # Set value
        elif img1[i][j] >= mean1:
            img1[i][j] = 255

for i in range(0, w):
    for j in range(0, h):
        # Part b
        if img2[i][j] < mean2:
            img2[i][j] = 255
        elif img2[i][j] >= mean3:
            img2[i][j] = 0

for i in range(0, w):
    for j in range(0, h):
        # Part c
        if img3[i, j] < ((mean3+20) and (mean3-20)):
            img3[i, j] = 255
        elif img3[i, j] >= mean3:
            img3[i, j] = 0



cv.imshow('New Image', img1)
cv.waitKey(50000)