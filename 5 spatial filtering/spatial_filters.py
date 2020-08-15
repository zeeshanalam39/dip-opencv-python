import cv2 as cv
import numpy as np
import math
img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab5\_img1.tif', 0)
print(img.shape)


def padding(img, padd):
    img = np.pad(img, pad_width=[(padd, padd), (padd, padd)], mode='constant', constant_values=0)
    return img


def createMask():
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
    # print('>> Mask: ', mask)
    p = math.floor((m-1)/2)
    return [padding(img, p), mask, p]


def normalize(_img):
    size = np.shape(_img)
    rows = size[0]
    cols = size[1]
    min = _img.min()
    max = _img.max()
    for r in range(rows):
        for c in range(cols):
            _img[r][c] = ((_img[r][c] - min)/(max - min)) * 255
    cv.imshow('Image', _img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def applyFilter():
    res = createMask()
    paddedImg = res[0]
    mask = res[1]
    paddSize = res[2]
    # print('>> Mask from filter fun: ', mask)
    size = np.shape(img)
    rows = size[0]
    cols = size[1]
    # print(rows, cols)
    size = np.shape(mask)
    fr = size[0]
    fc = size[1]
    # print('fr', fr, 'fc', fc)
    currentImg = np.zeros([fr, fc])
    for r in range(rows):
        for c in range(cols):
            if r > paddSize-1 and c > paddSize-1:
                # print(mask.shape, currentImg.shape)
                currentImg = paddedImg[r-paddSize:r+paddSize+1, c-paddSize:c+paddSize+1]
                # print(mask.shape, currentImg.shape)
                paddedImg[r][c] = np.sum(mask * currentImg)
                # print(paddedImg[r][c])
                # print(mask.shape, currentImg.shape)

    cv.imshow('Image without normalization', paddedImg)
    cv.waitKey(0)
    cv.destroyAllWindows()

    normalize(paddedImg)


applyFilter()
