import cv2 as cv    # Import packages
import numpy as np
import math

IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab9\_img2.tif', 0)     # Read img
cv.imshow('Original Image', IMAGE)  # Show img
cv.waitKey(0)
cv.destroyAllWindows()


def convert_to_binary(img, val):    # Function to convert gray scale img to binary img.
    size = np.shape(img)    # Get img size
    rows = size[0]
    cols = size[1]
    for r in range(0, rows):
        for c in range(0, cols):
            img[r][c] = 0 if img[r][c] < val else 1     # Store 0/1 in pxls.
    return img


def padding(_img, _p):  # Function to add padding
    _p = math.floor((_p-1)/2)   # Calculate padding size
    _img = np.pad(_img, pad_width=[(_p, _p), (_p, _p)], mode='constant', constant_values=0) # Add padding
    return _img


def erosion_dilation(img, erosion, dilation):
    p = int(input('Enter size of structuring element: '))   # get size of SE
    a = int(np.floor(p / 2))
    se = np.ones([p, p], dtype=np.uint8)
    img = padding(img, p)   # Add padding
    size = np.shape(img)    # Get img size
    rows = size[0]
    cols = size[1]
    currentImgWindow = np.zeros([p, p], dtype=np.uint8)     # Window of size SE
    img3 = np.zeros([rows, cols], dtype=np.uint8)   # New img to store results
    for r in range(p, rows-p):  # Perform erosion/dilation
        for c in range(p, cols-p):
            currentImgWindow[:, :] = img[r-a:r+a+1, c-a:c+a+1]  # Get window of size SE
            if erosion:     # Perform erosion if erosion is passed True in parameter.
                if np.sum(currentImgWindow) == (p * p): # Check for Fit condition
                    # img3[r-a:r+a+1, c-a:c+a+1] = 255
                    img3[r][c] = 255
                else:
                    # img3[r-a:r+a+1, c-a:c+a+1] = 0
                    img3[r][c] = 0
            if dilation:
                if (p * p) > np.sum(currentImgWindow) > 0:  # Check for Hit condition
                    # img3[r - a:r + a + 1, c - a:c + a + 1] = 255
                    img3[r][c] = 255
                else:
                    # img3[r-a:r+a+1, c-a:c+a+1] = 0
                    img3[r][c] = 0
    title = 'Eroded' if erosion else 'Dilated'  # Find img title according to input i.e., erosion/dilation
    cv.imshow(str(title + ' Image'), img3)  # Show result
    cv.waitKey(0)
    cv.destroyAllWindows()
    return img3


img2 = convert_to_binary(IMAGE, 150)    # Convert to binary
erodedImg = erosion_dilation(img2, True, False)     # Pass True first to erode img
erodedImg = convert_to_binary(erodedImg, 150)   # Convert to binary
erosion_dilation(erodedImg, False, True)    # Pass True in second argument
