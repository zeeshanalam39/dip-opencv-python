import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab4\_img3.tif', 0)
[w, h] = img.shape      # Get image rows & cols
histogram = list()      # Create empty lists
pdf = list()
cdf = list()
tf = list()
for p in range(0, 256):     # Append lists with 0
    histogram.append(0)
    pdf.append(0)
    cdf.append(0)
    tf.append(0)            # list with all zeros

for i in range(0, w):       # Histogram
    for j in range(0, h):
        histogram[img[i][j]] = histogram[img[i][j]] + 1
plt.plot(histogram)
plt.show()

for i in range(0, 256):     # PDF
    pdf[i] = histogram[i]/(w * h)
plt.plot(pdf)
plt.show()

for i in range(0, 256):     # CDF
    cdf[i] = sum(pdf[0:i])
plt.plot(cdf)
plt.show()

for i in range(0, 256):     # Transformation function
    tf[i] = round(cdf[i] * 255)
plt.plot(tf)
plt.show()

for i in range(w):          # Create contrast enhanced image
    for j in range(0, h):
        img[i][j] = tf[img[i][j]]
plt.plot(img)
plt.show()

for i in range(0, w):       # Histogram
    for j in range(0, h):
        histogram[img[i][j]] = histogram[img[i][j]] + 1
plt.plot(histogram)
plt.show()

cv.imshow('Enhanced', img)   # Show enhanced image
cv.waitKey(20000)




