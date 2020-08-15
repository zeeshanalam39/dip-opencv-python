import cv2 as cv    # Import packages
import numpy as np
import math

IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab9\_img3.tif', 0) # Read img
cv.imshow('Original Image', IMAGE)  # Show img
cv.waitKey(0)
cv.destroyAllWindows()


def padding(_img, _p):  # Function to add padding
    _p = math.floor((_p-1)/2)   # Find padding size
    _img = np.pad(_img, pad_width=[(_p, _p), (_p, _p)], mode='constant', constant_values=0) # Add padding
    return _img


def grayScale_ErosionDilation(img, erosion, dilation):
    p = int(input('Enter size of structuring element: '))   # Get size of SE
    a = int(np.floor(p / 2))
    img = padding(img, p)   # Add padding
    size = np.shape(img)    # get img size
    rows = size[0]
    cols = size[1]
    currentImgWindow = np.zeros([p, p], dtype=np.uint8)     # Create window of size: SE
    img2 = np.zeros([rows, cols], dtype=np.uint8)   # New img to store results
    for r in range(p, rows-p):  # Perform grayscale erosion/dilation
        for c in range(p, cols-p):
            currentImgWindow[:, :] = img[r-a:r+a+1, c-a:c+a+1]  # Get window of size SE
            if erosion:
                # img2[r-a:r+a+1, c-a:c+a+1] = np.min(currentImgWindow)
                img2[r][c] = np.min(currentImgWindow)   # Get min value from current window and store at pxl in new img
            if dilation:
                # img2[r-a:r+a+1, c-a:c+a+1] = np.max(currentImgWindow)
                img2[r][c] = np.max(currentImgWindow)   # Get max value from current window and store at pxl in new img

    title = 'Eroded/Min' if erosion else 'Dilated/Max'  # Find img title according to input i.e., erosion/dilation
    cv.imshow(str(title + ' Image'), img2)  # Show img
    cv.waitKey(0)
    cv.destroyAllWindows()
    return img2


eroded = grayScale_ErosionDilation(IMAGE, True, False)  # Call function to perform grayscale erosion.
dilated = grayScale_ErosionDilation(IMAGE, False, True)  # Call function to perform grayscale dilation
morphologicalGradient = dilated-eroded  # Calculate morphological grad.
cv.imshow('Morphological Gradient', morphologicalGradient)  # Show result.
cv.waitKey(0)
cv.destroyAllWindows()

