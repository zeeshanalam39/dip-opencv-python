import numpy as np
import cv2 as cv

img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab4\_img3.tif', 0)
p5 = np.percentile(img, 5)
p95 = np.percentile(img, 95)
[w, h] = img.shape
img1 = np.zeros([w, h, 3], dtype=np.uint8)

for i in range(0, w):
    for j in range(0, h):
        if img[i][j] < p5:
            img1[i][j] = 0
        elif img[i][j] > p95:
            img1[i][j] = 255
        else:
            img1[i][j] = ((img[i][j] - p5)/(p95 - p5)) * 255

cv.imshow('Original Image', img)
cv.imshow('New Image', img1)
cv.waitKey(20000)