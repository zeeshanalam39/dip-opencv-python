import cv2 as cv
import numpy as np
import math

img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab5\_img1.tif', 0)
print('Original Image Size', img.shape)


def padding(_img, padd):    # Add padding
    _img = np.pad(_img, pad_width=[(padd, padd), (padd, padd)], mode='constant', constant_values=0)
    return _img


def createMask():       # Create mask
    m = int(input('Enter mask size m: '))
    n = int(input('Enter mask size n: '))
    if m != n:
        print('Invalid mask size! Try again :)')
        createMask()
    mask = np.zeros([m, n], dtype=np.int_)
    for i in range(m):
        for j in range(n):
            mask[i][j] = int(input('Enter value for mask index: '))
    mask = mask/(m*n)
    p = math.floor((m-1)/2)     # Calculate padding size
    return [padding(img, p), mask, p]


def doubleThresholding(_newMagMtx, _rows, _cols):
    m = np.max(_newMagMtx)
    th = 0.2 * m    # High threshold
    tl = 0.1 * m    # Low threshold
    for r in range(_rows):
        for c in range(_cols):
            if _newMagMtx[r][c] <= tl:  # Replace with 1
                _newMagMtx[r][c] = 0
            elif _newMagMtx[r][c] >= th:    # Replace with 0
                _newMagMtx[r][c] = 1

    for r in range(_rows):      # For those values which are not in threshold
        for c in range(_cols):
            if _newMagMtx[r][c] != 0 and _newMagMtx[r][c] != 1:
                if (
                    _newMagMtx[r-1][c] == 1 or _newMagMtx[r+1][c] == 1 or _newMagMtx[r][c-1] == 1 or _newMagMtx[r][c+1] == 1 or
                    _newMagMtx[r-1][c-1] == 1 or _newMagMtx[r+1][c-1] == 1 or _newMagMtx[r-1][c+1] == 1 or _newMagMtx[r+1][c+1] == 1
                ):
                    _newMagMtx[r][c] = 1
                else:
                    _newMagMtx[r][c] = 0

    cv.imshow('Final image', _newMagMtx)
    cv.waitKey(0)
    cv.destroyAllWindows()




def nonMaxSuppression(_gradMag, _gradPhase):      # Performing non-maximum suppression.
    _gradMag = padding(_gradMag, 1)         # Add padding
    _gradPhase = padding(_gradPhase, 1)
    size = np.shape(_gradMag)
    _rows = size[0]
    _cols = size[1]
    newMagMtx = np.zeros([_rows, _cols])    # New matrix to store non-max suppression result.
    for r in range(_rows-1):
        for c in range(_cols-1):
            phase = _gradPhase[r][c]
            x = y = 0
            if (0 <= phase < 22.5) or (157.5 <= phase <= 180):  # Angle 0
                x = _gradMag[r][c+1]
                y = _gradMag[r][c-1]
            elif 22.5 <= phase < 67.5:      # Angle 45
                x = _gradMag[r+1, c-1]
                y = _gradMag[r-1, c+1]
            elif 67.5 <= phase < 112.5:     # Angle 90
                x = _gradMag[r+1, c]
                y = _gradMag[r-1, c]
            elif 112.5 <= phase < 157.5:    # Angle 135
                x = _gradMag[r-1, c-1]
                y = _gradMag[r+1, c+1]

            if (_gradMag[r][c] >= x) and (_gradMag[r][c] >= y):     # Replace gradient mag. values in new mag. mtx.
                newMagMtx[r][c] = _gradMag[r][c]
            else:
                newMagMtx[r][c] = 0

    cv.imshow('Non max suppression', newMagMtx)
    cv.waitKey(0)
    cv.destroyAllWindows()
    doubleThresholding(newMagMtx, _rows, _cols)


def sobels(_img):       # Performing sobel-x & sobel-y
    sobelX = cv.Sobel(_img, cv.CV_32F, 1, 0, ksize=3)
    sobelY = cv.Sobel(_img, cv.CV_32F, 0, 1, ksize=3)

    size = np.shape(sobelX)
    rows = size[0]
    cols = size[1]
    gradMag = np.zeros([rows, cols])    # Gradient magnitude
    gradPhase = np.zeros([rows, cols])  # Gradient phase

    for r in range(rows):
        for c in range(cols):
            gradMag[r][c] = math.sqrt((sobelX[r][c] ** 2 + sobelY[r][c] ** 2))      # Finding gradient magnitude
            gradPhase[r][c] = math.degrees(math.atan2(sobelY[r][c], sobelX[r][c]))  # Finding gradient phase

    cv.imshow('Gradient Magnitude', gradMag)
    cv.waitKey(0)
    cv.destroyAllWindows()
    nonMaxSuppression(gradMag, gradPhase)


def applyFilter():
    res = createMask()
    paddedImg = res[0]
    mask = res[1]
    paddSize = res[2]
    size = np.shape(img)
    rows = size[0]
    cols = size[1]
    size = np.shape(mask)   # Size of mask
    fr = size[0]
    fc = size[1]
    currentImg = np.zeros([fr, fc])     # Temporary array to store img portion to be multiplied by mask
    for r in range(rows-paddSize):
        for c in range(cols-paddSize):
            if r > paddSize-1 and c > paddSize-1:   # Ignore padded rows/cols
                currentImg = paddedImg[r-paddSize:r+paddSize+1, c-paddSize:c+paddSize+1]
                paddedImg[r][c] = np.sum(mask * currentImg)     # Multiply mask with respective img portion & replace in img pixel.

    cv.imshow('Image with Avg Filter', paddedImg)
    cv.waitKey(0)
    cv.destroyAllWindows()

    sobels(paddedImg)


applyFilter()
