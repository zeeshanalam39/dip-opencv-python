import cv2 as cv
import numpy as np

IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab7\_img1.png', 0)
print(IMAGE.shape)


def padding(axis, _m, p):   # Padd extra row/cow to end of img so that whole img has now equal size blocks
    while axis % _m != 0:   # If rows/cols cannot be divided equally into size of window.
        p = p + 1
    return p


def localMean(_img):
    m = int(input('Enter block/window size: '))     # get window size example 3*3
    size = np.shape(_img)   # Find img size
    rows = size[0]
    cols = size[1]
    paddCol = paddRow = 0

    paddRow = padding(rows, m, paddRow)     # Call padding() to add necessary padding.
    paddCol = padding(cols, m, paddCol)

    _img = np.pad(_img, pad_width=[(0, paddRow), (0, paddCol)], mode='constant', constant_values=0) # Padding rows/cols to end of img to adjust size
    size = np.shape(_img)   # Find size again after padding
    rows = size[0]
    cols = size[1]
    meanImg = np.zeros([rows, cols], dtype=np.uint8)    # New img
    blockImg = np.zeros([m, m], dtype=np.uint8)         # to store 3*3 block of img
    mean = 0
    for r in range(0, rows, m):
        for c in range(0, cols, m):
            blockImg = _img[r:r+m, c:c+m]   # Getting 3*3 block of img
            mean = int(np.mean(blockImg)) - 3  # Mean
            for x in range(0, m, 1):        # Creating loop to make new img
                for y in range(0, m, 1):
                    meanImg[x+r][y+c] = 0 if blockImg[x][y] < mean else 255     # Fill new img with 0 OR 255

    cv.imshow('Local Mean', meanImg)    # Show image
    cv.waitKey(0)
    cv.destroyAllWindows()


localMean(IMAGE)


