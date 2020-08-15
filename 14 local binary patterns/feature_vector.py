import numpy as np  # Importing packages
import cv2 as cv
from matplotlib import pyplot as plt

IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab15/_me.jpg', 0)  # Reading image


def padding(image, paddingsize):  # Adding padding
    padded_img = np.pad(image, (paddingsize, paddingsize), "constant")
    return padded_img


padded_img = padding(IMAGE, 1)  # Call function to add padding

lbp_image = np.zeros(shape=(np.shape(padded_img)), dtype='uint8')  # Creating output image to store lbp
decimal_array = []
window = []


def threshold(pt, pt1, pt2, pt3, pt4, pt5, pt6, pt7):  # generating array of calculated 1 and 0
    array = [pt, pt1, pt2, pt3, pt4, pt5, pt6, pt7]
    return array


def local_binary_pattern(image, pad_size):  # Function to calculate LBP
    row, col = np.shape(image)  # Get image size
    row_end = row - pad_size
    col_end = col - pad_size
    for i in range(pad_size, row_end):
        for j in range(pad_size, col_end):
            window[:] = image[i - pad_size:i + pad_size + 1, j - pad_size:j + pad_size + 1]  # window will contain 3*3 image values in it
            center_value = window[1][1]  # finding center values
            window_array = np.array(window)  # converting to array

            if window_array[0][0] < center_value:  # if window specific pixel has value less than center values it will put 0 and if greater than center then it will put 1
                pt = 0
            if window_array[0][0] >= center_value:
                pt = 1

            if window_array[0][1] < center_value:
                pt1 = 0
            if window_array[0][1] >= center_value:
                pt1 = 1

            if window_array[0][2] < center_value:
                pt2 = 0
            if window_array[0][2] >= center_value:
                pt2 = 1

            if window_array[1][2] < center_value:
                pt3 = 0
            if window_array[1][2] >= center_value:
                pt3 = 1

            if window_array[2][2] < center_value:
                pt4 = 0
            if window_array[2][2] >= center_value:
                pt4 = 1

            if window_array[2][1] < center_value:
                pt5 = 0
            if window_array[2][1] >= center_value:
                pt5 = 1

            if window_array[2][0] < center_value:
                pt6 = 0
            if window_array[2][0] >= center_value:
                pt6 = 1

            if window_array[1][0] < center_value:
                pt7 = 0
            if window_array[1][0] >= center_value:
                pt7 = 1

            calculated_center_decimal = []
            calculated_center_decimal = threshold(pt, pt1, pt2, pt3, pt4, pt5, pt6, pt7)  # calling funtion
            weight_array = [128, 64, 32, 16, 8, 4, 2, 1]  # setting a weight array
            result = []
            result = np.array(calculated_center_decimal) * np.array(weight_array)  # element wise multipication with weight array
            resultant_center_value = np.sum(result)

            lbp_image[i][j] = resultant_center_value  # Storing LBP value in lbp_image
    return lbp_image


lbp_image = local_binary_pattern(padded_img, 1)  # Calling function to get LBP

cv.imshow('LBP', lbp_image)  # Show result
cv.waitKey()
cv.destroyAllWindows()

plt.hist(lbp_image.ravel(), 64, [0, 256])
plt.show()
