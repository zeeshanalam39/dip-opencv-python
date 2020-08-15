import cv2 as cv
import numpy as np

img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\images\_a1.jpg', 0)   # Read image
[w, h] = img.shape                              # Read image size
newImage = np.zeros([w, h, 3], dtype=np.uint8)  # Create new image
g = [0.2, 0.5, 1.2, 1.8, 3.2]                   # gamma values
newImage = 255 * np.power((img/255), g[4])      # Perform power law transformation
newImage = np.array(img, dtype=np.uint8)        # Reset data type
cv.imshow('Image', newImage)                    # Show image
cv.waitKey(50000)