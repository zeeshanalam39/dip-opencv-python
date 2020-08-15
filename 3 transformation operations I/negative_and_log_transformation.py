import cv2 as cv
import numpy as np
# Part a
img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab3\es.tif', 0)    # Read image
cv.imshow('Old Image', img)
cv.waitKey(5000)
[w, h] = img.shape                                # Find image size
newImg = np.zeros([w, h, 3], dtype=np.uint8)      # create image
newImg.fill(0)                                    # MAke it darker
newImg = 255 - img                                # Perform -ve transformation
cv.imshow('New Image', newImg)
cv.waitKey(50000)

# Part b
# img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab3\es.tif', 0)
# cv.imshow('Old Image', img)
# cv.waitKey(5000)
# c = 255/(np.log(1 + np.max(img)))               # Find c
# newImage = c * np.log(img + 1)                  # Perform Log Transformation
# newImage = np.array(newImage, dtype=np.uint8)   # Set data type
# cv.imshow('New Image', newImage)
# cv.waitKey(50000)