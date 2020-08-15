import cv2 as cv
import numpy as np
import math

img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab5\_img2.tif', 0)
cv.imshow('Original Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
print(img.shape)


def padding(_img, padd):    # Function to add padding.
    _img = np.pad(_img, pad_width=[(padd, padd), (padd, padd)], mode='constant', constant_values=0)
    return _img


def createMask(_img):
    m = int(input('Enter mask size m: '))
    n = int(input('Enter mask size n: '))
    if m != n:
        print('Invalid mask size! Try again :)')
        createMask()
    mask = np.zeros([m, n], dtype=np.int_)
    for i in range(m):
        for j in range(n):
            mask[i][j] = int(input('Enter value for mask index: '))
    mask = mask / (m * n)
    p = math.floor((m - 1) / 2)
    return [padding(img, p), mask, p]


def sobelGradient(_img, _paddSize):
    sX = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])
    sY = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    print(_img.shape)
    _img = padding(_img, 1)
    size = np.shape(_img)
    rows = size[0]
    cols = size[1]
    print(_img.shape)
    size = np.shape(sX)
    fr = size[0]
    fc = size[1]
    currentImg = np.zeros([fr, fc])
    for r in range(rows-_paddSize):
        for c in range(cols-_paddSize):
            if r > _paddSize-1 and c > _paddSize-1:
                currentImg = _img[r-_paddSize:r+_paddSize+1, c-_paddSize:c+_paddSize+1]
                _img[r][c] = np.sum(sX * sY * currentImg)

    cv.imshow('Sobel Gradient', _img)
    cv.waitKey(0)
    cv.destroyAllWindows()




def sharpenedImage(_lap, _img, _paddSize):      # Making image sharp(original + laplacian)
    print(_lap.shape)
    print(_img.shape)
    size = np.shape(_img)
    rows = size[0]
    cols = size[1]
    _lap = np.delete(_lap, 0, 0)        # Deleting padded rows/cols
    _lap = np.delete(_lap, rows-1, 0)
    _lap = np.delete(_lap, 0, 1)
    _lap = np.delete(_lap, cols-1, 1)
    print(_lap.shape)
    print(_img.shape)
    shrapImg = np.zeros([rows, cols])
    for r in range(rows):               # Adding both
        for c in range(cols):
            shrapImg[r][c] = _lap[r][c] + _img[r][c]

    cv.imshow('Sharpened', shrapImg)
    cv.waitKey(0)
    cv.destroyAllWindows()

    choice = int(input('Press 1 for sobel gradient!: '))
    if choice == 1:
        print('You went for sobel gradient :)')
        sobelGradient(shrapImg, _paddSize)




def laplacian(_img):
    res = createMask(_img)
    paddedImg = res[0]
    mask = res[1]
    paddSize = res[2]
    size = np.shape(paddedImg)
    rows = size[0]
    cols = size[1]
    print(rows, cols)
    size = np.shape(mask)
    fr = size[0]
    fc = size[1]
    currentImg = np.zeros([fr, fc])
    for r in range(rows-paddSize):
        for c in range(cols-paddSize):
            if r > paddSize-1 and c > paddSize-1:
                currentImg = paddedImg[r-paddSize:r+paddSize+1, c-paddSize:c+paddSize+1]
                paddedImg[r][c] = np.sum(mask * currentImg)

    cv.imwrite('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab5\Laplacian.tif', paddedImg)
    cv.imshow('Laplacian', paddedImg)
    cv.waitKey(0)
    cv.destroyAllWindows()

    print('Do you want to create sharpened image(Original+Laplacian)? Press 1! :)')
    choice = int(input('Enter 1 for sharp image: '))
    if choice == 1:
        print('You went for sharp image. :)')
    sharpenedImage(paddedImg, img, paddSize)      # Calling function to create sharpened image




laplacian(img)
# cv.imshow('...', img)
# cv.waitKey(0)
# cv.destroyAllWindows()
