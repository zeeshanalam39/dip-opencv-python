import cv2 as cv
import numpy as np

img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab6\_img2.tif', 0)
edges = cv.Canny(img, 50, 150, apertureSize=3)

lines = cv.HoughLines(edges, 1, np.pi/180, 200)
for rho, theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000 * a)

    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
