import cv2 as cv    # Importing opencv package
import numpy as np  # Importing numpy
import math

# img 01
# IMAGE1 = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab10\_img1.tif')  # Read coloured img
# cv.imshow('Original Image', IMAGE1)     # Show img
# cv.waitKey()
# cv.destroyAllWindows()

# img 02
IMAGE1 = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab10\_img2.tif')  # Read coloured img
cv.imshow('Original Image', IMAGE1)  # Show img
cv.waitKey()
cv.destroyAllWindows()

red_channel,  green_channel, blue_channel = cv.split(IMAGE1)     # Extracting RGB Channels & Showing them
blue_channel = blue_channel/255     # Normalizing channels
green_channel = green_channel/255
red_channel = red_channel/255

size = np.shape(blue_channel)   # Get shape of channel.
print(size)
rows = size[0]
cols = size[1]
hue = np.zeros([rows, cols])        # Creating matrices to store hue, saturation & intensity
saturation = np.zeros([rows, cols])
intensity = np.zeros([rows, cols])

for r in range(rows):       # Calculating hue, saturation & intensity.
    for c in range(cols):
        numerator = ((red_channel[r][c]-green_channel[r][c]) + (red_channel[r][c]-blue_channel[r][c]))/2
        denominator = math.sqrt(((red_channel[r][c]-green_channel[r][c])**2) + (red_channel[r][c]-blue_channel[r][c])*(green_channel[r][c]-blue_channel[r][c]))
        theta = numerator/denominator
        theta = math.acos(theta)
        theta = math.degrees(theta)
        if blue_channel[r][c] <= green_channel[r][c]:
            hue[r][c] = theta
        elif blue_channel[r][c] > green_channel[r][c]:
            hue[r][c] = 360-theta
        min_RGB = min(red_channel[r][c], green_channel[r][c], blue_channel[r][c])
        saturation[r][c] = 1-(3/(red_channel[r][c] + green_channel[r][c] + blue_channel[r][c])) * min_RGB
        intensity[r][c] = (red_channel[r][c] + green_channel[r][c] + blue_channel[r][c])/3

# hsvv = cv.cvtColor(IMAGE1, cv.COLOR_BGR2HSV)
# hue,s,v = cv.split(hsvv)

cv.imshow('Hue', hue)   # Show hue
cv.waitKey()
cv.destroyAllWindows()

cv.imshow('Saturation', saturation)     # Show saturation
cv.waitKey()
cv.destroyAllWindows()

cv.imshow('Intensity', intensity)       # Show intensity
cv.waitKey()
cv.destroyAllWindows()

hsv = cv.merge([hue, saturation, intensity])    # Merging hue, saturation, intensity to make HSV img.
cv.imshow('HSV', hsv)
cv.waitKey()
cv.destroyAllWindows()


