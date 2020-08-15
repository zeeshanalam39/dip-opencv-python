# import cv2 as cv
# import numpy as np
# import math

# IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab11\_img5.tif', 0)
# cv.imshow('Original Image', IMAGE)
# cv.waitKey()
# cv.destroyAllWindows()
#
# fft = np.zeros(IMAGE.shape, dtype=np.float32)
# fft = np.fft.fft2(np.float32(IMAGE))
# fft = np.fft.fftshift(fft)
# fft_shifted = np.zeros(IMAGE.shape, dtype=np.float32)
# fft_shifted = fft
# fft = np.abs(fft)
# fft = np.log(fft)
# fft = cv.normalize(fft, 0, 255, cv.NORM_MINMAX)
#
# cv.imshow('FFT', fft)
# cv.waitKey()
# cv.destroyAllWindows()
#
# size = np.shape(fft)
# rows = size[0]
# cols = size[1]
# final_image = np.zeros([rows, cols], dtype=np.float32)
# cut_off = 30
# high_pass_filter = np.ones([rows, cols], dtype=np.float32)
# c1 = math.floor(rows/2)
# c2 = math.floor(cols/2)
# high_pass_filter[c1-cut_off:c1+cut_off, c2-cut_off:c2+cut_off] = 0
# final_image = fft_shifted*high_pass_filter
# final_image = np.fft.ifft2(final_image)
# final_image = np.abs(final_image)
# final_image = cv.normalize(final_image, 0, 255, cv.NORM_MINMAX)
# final_image = np.float32(final_image)
# final_image = IMAGE + final_image - 2   # For Img 05
#
# cv.imshow('Final Image', final_image)
# cv.waitKey()
# cv.destroyAllWindows()


# ==============================================================================================
#                                   ----- Moon Img -----
# ==============================================================================================
import cv2 as cv
import numpy as np
import math

IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab11\_img6.tif', 0)
cv.imshow('Original Image', IMAGE)
cv.waitKey()
cv.destroyAllWindows()

fft = np.zeros(IMAGE.shape, dtype=np.float32)
fft = np.fft.fft2(np.float32(IMAGE))
fft = np.fft.fftshift(fft)
fft_shifted = np.zeros(IMAGE.shape, dtype=np.float32)
fft_shifted = fft
fft = np.abs(fft)
fft = np.log(fft)
fft = cv.normalize(fft, 0, 255, cv.NORM_MINMAX)

cv.imshow('FFT', fft)
cv.waitKey()
cv.destroyAllWindows()

size = np.shape(fft)
rows = size[0]
cols = size[1]
final_image = np.zeros([rows, cols], dtype=np.float32)
cut_off = 50
high_pass_filter = np.zeros([rows, cols], dtype=np.float32)
c1 = math.floor(rows/2)
c2 = math.floor(cols/2)
high_pass_filter[c1-cut_off:c1+cut_off, c2-cut_off:c2+cut_off] = 1
final_image = fft_shifted*high_pass_filter
final_image = np.fft.ifft2(final_image)
final_image = np.abs(final_image)
final_image = cv.normalize(final_image, 0, 255, cv.NORM_MINMAX)
final_image = np.float32(final_image)
k = 7
final_image = cv.GaussianBlur(final_image, (k, k), 0)

cv.imshow('Final Image', final_image)
cv.waitKey()
cv.destroyAllWindows()






