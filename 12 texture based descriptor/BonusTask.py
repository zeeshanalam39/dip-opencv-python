import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab12\_img1.tif', 0)
IMAGE = np.float32(IMAGE)
rows, cols = np.shape(IMAGE)
fourier_image = np.fft.fft2(IMAGE)
dc_shifted = np.fft.fftshift(fourier_image)
dc1_shifted = np.zeros(shape=(rows, cols), dtype=np.float32)
dc1_shifted = dc_shifted
log_image = abs(dc_shifted)
log_image = np.log(log_image)
min = np.min(log_image)
max = np.max(log_image)
outputimage = np.zeros(shape=(rows, cols), dtype=np.float32)
outputimage = cv.normalize(log_image, 0, 255, cv.NORM_MINMAX)


sumarray=[]
rows, cols = np.shape(log_image)
print(rows)
arrayxaxis = []
center = rows/2
temp = np.zeros(shape=(rows, cols), dtype=np.uint8)
i = 0
sum1 = []
sum2 = []
for p in range(200):
    sum1[:] = log_image[p:rows-p][p]
    sum2[:] = log_image[p][p:rows-p]
    print(p)
    sumt = np.sum(sum1)
    sumk = np.sum(sum2)
    sum = (2*sumk)+(2*sumt)
    sumarray.append(sum)
    if p == 300:
        break
for k in range(0, 200):
    arrayxaxis.append(k)
print(sumarray)
reverse = sumarray[::-1]
print(arrayxaxis)

plt.plot(arrayxaxis, reverse)
plt.show()

