import cv2 as cv
import numpy as np

img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab1\_girl.tif', 0)
[w, h] = img.shape
img1 = np.zeros([w, h, 3], dtype=np.uint8)
img2 = np.zeros([w, h, 3], dtype=np.uint8)
img3 = np.zeros([w, h, 3], dtype=np.uint8)

# Flipped Vertically
r = w - 1
for i in range(0, w):
    c = 0
    for j in range(0, h):
        img1[r][c] = img[i][j]
        if c <= h:
            c = c + 1
    r = r - 1

# Flipped Horizontally
r = c = 0
c = h - 1
for i in range(0, w):
    c = 0
    for j in range(0, h):
        img2[r][c] = img[i][j]
        c = c - 1
    r = r + 1

# Flipped Both
r = c = 0
r = w - 1
c = h - 1
for i in range(0, w):
    c = 0
    for j in range(0, h):
        img3[r][c] = img[i][j]
        c = c - 1
    r = r - 1


cv.imshow('Original Image', img)
cv.imshow('Flipped Vertically', img1)
cv.imwrite('Flipped Vertically.tif', img1)

# cv.imshow('Flipped Horizontally', img2)
# cv.imwrite('Flipped Horizontally.tif', img2)

# cv.imshow('Flipped Both', img3)
# cv.imwrite('Flipped Both.tif', img3)

cv.waitKey(20000)
cv.destroyAllWindows()