import cv2 as cv
import numpy as np

IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab11\_img1.tif', 0)
# IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab11\_img2.tif', 0)
cv.imshow('Original Image', IMAGE)
cv.waitKey()
cv.destroyAllWindows()

fft = np.zeros(IMAGE.shape, dtype=np.float32)
fft = np.fft.fft2(np.float32(IMAGE))
fft = np.fft.fftshift(fft)
fft = np.abs(fft)
# fft = np.log(fft)
# fft = cv.normalize(fft, None)
size = np.shape(fft)
rows = size[0]
cols = size[1]
min_ = np.min(fft)
max_ = np.max(fft)
for r in range(rows):
    for c in range(cols):
        fft[r][c] = ((fft[r][c]-min_)/(max_-min_)) * 255

cv.imshow('FFT', fft)
cv.waitKey()
cv.destroyAllWindows()

