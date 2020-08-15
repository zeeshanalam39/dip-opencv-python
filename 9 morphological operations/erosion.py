import cv2 as cv    # Importing packages
import numpy as np
import math

IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab9\_img1.jpg', 0) # Reading img
cv.imshow('Original Image', IMAGE)  # Showing img
cv.waitKey(0)
cv.destroyAllWindows()


def convert_to_binary(img, val):    # Converting gray scale img to binary img.
    size = np.shape(img)    # Finding img size.
    rows = size[0]
    cols = size[1]
    for r in range(0, rows):
        for c in range(0, cols):
            img[r][c] = 0 if img[r][c] < val else 1 # Assigning pxls 0/1.
    return img


def padding(_img, _p):  # Function to add padding.
    _p = math.floor((_p-1)/2)   # Finding padding size.
    _img = np.pad(_img, pad_width=[(_p, _p), (_p, _p)], mode='constant', constant_values=0) # Add padding.
    return _img


def erosion(img):
    p = int(input('Enter size of structuring element: '))   # Get structuring element size.
    a = int(np.floor(p / 2))
    se = np.ones([p, p], dtype=np.uint8)    # Make SE
    img = padding(img, p)   # Add padding
    size = np.shape(img)    # Get img size
    rows = size[0]
    cols = size[1]
    currentImgWindow = np.zeros([p, p], dtype=np.uint8) # Window of size SE
    img3 = np.zeros([rows, cols], np.uint8)     # New img to store result
    for r in range(p, rows-p):  # Perform erosion
        for c in range(p, cols-p):
            currentImgWindow[:, :] = img[r-a:r+a+1, c-a:c+a+1]  # Get window of size SE
            if np.sum(currentImgWindow) == (p*p):   # Check for Fit condition.
                # img3[r-a:r+a+1, c-a:c+a+1] = 255
                img3[r][c] = 255    # Store 255 in case of Fit
            else:
                # img3[r-a:r+a+1, c-a:c+a+1] = 0
                img3[r][c] = 0  # Store 0 if Fit does not happen.
    return img3


img2 = convert_to_binary(IMAGE, 150)    # Call function to binirize img.
img2 = erosion(img2)    # Call erosion function.

cv.imshow('Eroded Image', img2)     # Show eroded img.
cv.waitKey(0)
cv.destroyAllWindows()
