import cv2 as cv
import numpy as np
import math
img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab5\_img4.png', 0)
print(img.shape)
cv.imshow('Original Image', img)
cv.waitKey(0)
cv.destroyAllWindows()


def padding(imgPadd, padd):     # Function to add zeros
    print('>> Size before padding: ', imgPadd.shape)
    imgPadd = np.pad(imgPadd, pad_width=[(padd, padd), (padd, padd)], mode='constant', constant_values=0)
    print('>> Size after padding: ', imgPadd.shape)
    return imgPadd


def createMask():               # Mask related work
    m = int(input('Enter mask size m: '))
    n = int(input('Enter mask size n: '))
    if m != n:      # Check for valid mask size
        print('Invalid mask size! Try again :(')
        createMask()
    p = math.floor((m-1)/2)     # Find padding size
    return [padding(img, p), p, m]  # Return padding img, padding size & mask size


def applyFilter(choice):
    res = createMask()
    paddedImg = res[0]  # Padded Img
    paddSize = res[1]   # Padding Size
    fr = fc = res[2]    # Filter Size
    i = math.ceil((fr * fc) / 2) - 1    # Middle value of sorted array for Median filter
    size = np.shape(img)
    rows = size[0]
    cols = size[1]
    print(rows, cols)
    currentImg = np.zeros([fr, fc])
    for r in range(rows):
        for c in range(cols):
            if choice == 3:     # Median Filter
                if r > paddSize-1 and c > paddSize-1:
                    currentImg = paddedImg[r-paddSize:r+paddSize+1, c-paddSize:c+paddSize+1]
                    paddedImg[r][c] = np.sort(currentImg.flatten())[i]
            elif choice == 1:   # Min Filter
                if r > paddSize - 1 and c > paddSize - 1:
                    currentImg = paddedImg[r - paddSize:r + paddSize + 1, c - paddSize:c + paddSize + 1]
                    paddedImg[r][c] = np.amin(currentImg)

            elif choice == 2:   # Max Filter
                if r > paddSize - 1 and c > paddSize - 1:
                    currentImg = paddedImg[r - paddSize:r + paddSize + 1, c - paddSize:c + paddSize + 1]
                    paddedImg[r][c] = np.max(currentImg)

            else:               # Mean Filter
                if r > paddSize - 1 and c > paddSize - 1:
                    currentImg = paddedImg[r - paddSize:r + paddSize + 1, c - paddSize:c + paddSize + 1]
                    paddedImg[r][c] = np.mean(currentImg)


    cv.imshow('Image', paddedImg)
    cv.waitKey(0)
    cv.destroyAllWindows()


def selectFilter():
    choice = int(input('Enter filter to apply: 1 for min, 2 for max, 3 for median, 4 for mean.: '))
    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        applyFilter(choice)
    else:
        print('ERROR: Invalid choice. Try again :(')
        selectFilter()


selectFilter()
while True:
    runAgain = int(input('Press 1 to run again OR 0 to exit! : '))
    if runAgain == 1:
        selectFilter()
    else:
        print('Good Bye :)')
        break
