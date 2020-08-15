import cv2 as cv
import numpy as np

img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab3\Picture1.png', 0)  # Read image
[w, h] = img.shape
img1 = np.zeros([w, h, 3], dtype=np.uint8)
img2 = np.zeros([w, h, 3], dtype=np.uint8)
img3 = np.zeros([w, h, 3], dtype=np.uint8)
img4 = np.zeros([w, h, 3], dtype=np.uint8)
img5 = np.zeros([w, h, 3], dtype=np.uint8)
img6 = np.zeros([w, h, 3], dtype=np.uint8)
img7 = np.zeros([w, h, 3], dtype=np.uint8)
img8 = np.zeros([w, h, 3], dtype=np.uint8)

def bitget(nbr, pos):
    return (nbr >> pos) & 1

planes = 8
for i in range(0, w):
    for j in range(0, h):
        for p in range(planes - 1, -1, -1):
            if p == 7:
                img1[i][j] = 255 * bitget(img[i][j], p)
            elif p == 6:
                img2[i][j] = 255 * bitget(img[i][j], p)
            elif p == 5:
                img3[i][j] = 255 * bitget(img[i][j], p)
            elif p == 4:
                img4[i][j] = 255 * bitget(img[i][j], p)
            elif p == 3:
                img5[i][j] = 255 * bitget(img[i][j], p)
            elif p == 2:
                img6[i][j] = 255 * bitget(img[i][j], p)
            elif p == 1:
                img7[i][j] = 255 * bitget(img[i][j], p)
            else:
                img8[i][j] = 255 * bitget(img[i][j], p)


cv.imshow('Plane08', img1)
cv.imshow('Plane07', img2)
cv.imshow('Plane06', img3)
cv.imshow('Plane05', img4)
cv.imshow('Plane04', img5)
cv.imshow('Plane03', img6)
cv.imshow('Plane02', img7)
cv.imshow('Plane01', img8)
cv.waitKey(50000)