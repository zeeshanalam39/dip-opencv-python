import cv2 as cv
import numpy as np
import math

img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab6\_img3.tif', 0)


def sobels(_choice):
    sobelX = cv.Sobel(img, cv.CV_32F, 1, 0, ksize=3)
    sobelY = cv.Sobel(img, cv.CV_32F, 0, 1, ksize=3)

    size = np.shape(sobelX)
    rows = size[0]
    cols = size[1]
    gradMag = np.zeros([rows, cols])
    gradPhase = np.zeros([rows, cols])

    for r in range(rows):
        for c in range(cols):
            gradMag[r][c] = math.sqrt((sobelX[r][c] ** 2 + sobelY[r][c] ** 2))
            gradPhase[r][c] = math.degrees(math.atan2(sobelY[r][c], sobelX[r][c]))

    top30 = 0.70 * gradMag.max()
    for r in range(rows):
        for c in range(cols):
            # ----- Top 30% -----
            if _choice == 1:
                if gradMag[r][c] >= top30:
                    gradMag[r][c] = gradMag[r][c]
                else:
                    gradMag[r][c] = 0

            # ----- 45/90 Degrees -----
            elif _choice == 2:
                if gradPhase[r][c] == 45 or gradPhase[r][c] == 90:
                    gradMag[r][c] = gradMag[r][c]
                else:
                    gradMag[r][c] = 0

            # ----- Top 30% & 45/90 Degrees
            else:
                if gradMag[r][c] >= top30 and (gradPhase[r][c] == 45 or gradPhase[r][c] == 90):
                    gradMag[r][c] = gradMag[r][c]
                else:
                    gradMag[r][c] = 0

    cv.imshow('Image', gradMag)
    cv.waitKey(0)
    cv.destroyAllWindows()
    print(sobelX.shape)
    print(sobelY.shape)
    print(gradMag.shape)
    print(top30)


while True:
    print('You can enter 0 to exit!')
    choice = int(input('Enter 1 for top 30% only, 2 for 45/90 degrees only, 3 for both top 30% & 45/90 degrees!: '))
    if choice > 0:
        sobels(choice)
    else:
        print('You chose to exit!')
        break
