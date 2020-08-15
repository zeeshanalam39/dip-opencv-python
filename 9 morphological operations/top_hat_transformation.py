import cv2 as cv
import numpy as np
import math

IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab9\_img4.tif', 0)
cv.imshow('Original Image', IMAGE)
cv.waitKey(0)
cv.destroyAllWindows()


def threshold(img, val):
    size = np.shape(img)
    rows = size[0]
    cols = size[1]
    for r in range(0, rows):
        for c in range(0, cols):
            img[r][c] = 0 if img[r][c] < val else 255
    return img


def padding(_img, _p):
    _p = math.floor((_p-1)/2)
    _img = np.pad(_img, pad_width=[(_p, _p), (_p, _p)], mode='constant', constant_values=0)
    return _img


def erosion_dilation(img, erosion, dilation):
    p = int(input('Enter size of structuring element: '))
    a = int(np.floor(p / 2))
    # img = padding(img, p)
    size = np.shape(img)
    rows = size[0]
    cols = size[1]
    currentImgWindow = np.zeros([p, p], dtype=np.uint8)
    img2 = np.zeros([rows, cols], dtype=np.uint8)
    for r in range(p, rows - p):
        for c in range(p, cols - p):
            currentImgWindow[:, :] = img[r-a:r+a+1, c-a:c+a+1]
            if erosion:
                # img2[r-a:r+a+1, c-a:c+a+1] = np.min(currentImgWindow)
                img2[r][c] = np.min(currentImgWindow)
            if dilation:
                # img2[r-a:r+a+1, c-a:c+a+1] = np.max(currentImgWindow)
                img2[r][c] = np.max(currentImgWindow)

    title = 'Eroded' if erosion else 'Dilated/Opening'
    cv.imshow(str(title + ' Image'), img2)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return img2


erodedImg = erosion_dilation(IMAGE, True, False)        # Eroding
dilatedImg = erosion_dilation(erodedImg, False, True)   # Dilating
topHat = IMAGE-dilatedImg       # Top hat
cv.imshow('Top Hat', topHat)    # Showing top hat result
cv.waitKey()
cv.destroyAllWindows()

topHat = threshold(topHat, 60)
cv.imshow('Threshold', topHat)
cv.waitKey()
cv.destroyAllWindows()

