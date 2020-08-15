import cv2 as cv    # Importing packages
import numpy as np
from skimage.feature import greycomatrix, greycoprops

# IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab12\_img1.tif', 0)    # Reading images
# IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab12\_img2.tif', 0)
IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab12\_img3.tif', 0)
cv.imshow('Image', IMAGE)
cv.waitKey()
cv.destroyAllWindows()

result = greycomatrix(IMAGE, [1], [0], levels=256)      # Calculating co-matrix
my_GLCM = result[:, :, 0, 0]
print(my_GLCM)

c = greycoprops(result, prop='contrast')    # Getting contrast
print('Contrast: ', c[0, 0])
e = greycoprops(result, prop='energy')      # Getting energy
print('Energy', e[0, 0])
h = greycoprops(result, prop='homogeneity')     # Getting homogeneity
print('Homogeneity: ', h[0, 0])
co = greycoprops(result, prop='correlation')    # Getting correlation
print('Correlation: ', co[0, 0])
d = greycoprops(result, prop='dissimilarity')   # Dissimilarity
print('Dissimilarity: ', d[0, 0])


