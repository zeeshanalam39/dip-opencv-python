import cv2 as cv
import numpy as np

IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab7\_img1.png', 0)
print(IMAGE.shape)


def padding(axis, _m, p):   # Padd extra row/cow to end of img so that whole img has now equal size blocks
    while axis % _m != 0:   # If rows/cols cannot be divided equally into size of window.
        p = p + 1
    return p


def localAdaptiveThresholding(_img, epsilon):
    m = int(input('Enter block/window size: '))  # get window size example 3*3
    paddCol = paddRow = 0
    size = np.shape(_img)  # Find img size
    rows = size[0]
    cols = size[1]

    # paddRow = padding(rows, m, paddRow)  # Call padding() to add necessary padding.
    # paddCol = padding(cols, m, paddCol)
    paddCol = 1
    _img = np.pad(_img, pad_width=[(0, paddRow), (0, paddCol)], mode='constant', constant_values=0) # Padding rows/cols to end of img to adjust size
    size = np.shape(_img)  # Find img size
    rows = size[0]
    cols = size[1]

    newImg = np.zeros([rows, cols], dtype=np.uint8)  # New img
    blockImg = np.zeros([m, m], dtype=np.uint8)  # to store 3*3 block of img
    group1 = group2 = []  # Lists to store groups

    print('Main Loop!')
    for r in range(0, rows, m):
        print('Main Loop inside!')
        for c in range(0, cols, m):
            nextThreshold = prevThreshold = m1 = m2 = 0
            group1 = group2 = []
            blockImg = _img[r:r+m, c:c+m]   # Getting 3*3 block of sub img
            prevThreshold = int(np.mean(blockImg))  # Mean of 3*3 sub img

            for x in range(0, m):  # Initial thresholding
                print('Initial Th')
                for y in range(0, m):
                    print('Initial Th inside!')
                    if _img[x][y] < prevThreshold:
                        group1.append(blockImg[x][y])
                    else:
                        group2.append(blockImg[x][y])

            m1 = sum(group1) / len(group1)  # Find mean of each group
            m2 = sum(group2) / len(group2)
            nextThreshold = (m1 + m2) / 2  # Find new threshold

            print('while.........................................')
            while abs(nextThreshold - prevThreshold) >= epsilon:  # Keep going if condition is not satisfied.
                print('Inside while**********************************')
                group1 = group2 = []  # Clear groups

                for a in range(0, m):  # Again threshold
                    print('Again Th..............................')
                    for b in range(0, m):
                        print('Again Th inside!')
                        if blockImg[a][b] < nextThreshold:
                            group1.append(_img[a][b])
                        else:
                            group2.append(_img[a][b])

                prevThreshold = nextThreshold
                m1 = sum(group1) / len(group1)  # Find mean of each group
                m2 = sum(group2) / len(group2)
                nextThreshold = (m1 + m2) / 2

            print('Creating new image')
            for x in range(0, m, 1):        # Creating loop to make new img
                for y in range(0, m, 1):
                    newImg[x+r][y+c] = 0 if blockImg[x][y] < nextThreshold - 2 else 255     # Fill new img with 0 OR 255
            print('New block filled!')


    cv.imshow('Local Adaptive Thresholding', newImg)    # Show image
    cv.waitKey(0)
    cv.destroyAllWindows()


localAdaptiveThresholding(IMAGE, 8)
