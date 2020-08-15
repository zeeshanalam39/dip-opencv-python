import numpy as np
import cv2 as cv
img = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab2\Picture6.png', 0)
rows = np.size(img, 0)
cols = np.size(img, 1)
labelMtx = np.zeros([rows, cols], dtype=np.uint16)
eqMtx = []
label = 0

for i in range(rows):
    for j in range(cols):
        if img[i][j] >= 127:
            img[i][j] = 1
        else:
            img[i][j] = 0

for r in range(rows):
    for c in range(cols):
        if img[r][c] == 1:
            if img[r][c-1] == 0 and img[r-1][c] == 0:
                label = label+1
                eqMtx.append(label)
                labelMtx[r][c] = label
            elif img[r][c - 1] == 1 and img[r - 1][c] == 0:
                labelMtx[r][c] = labelMtx[r][c-1]
            elif img[r][c - 1] == 0 and img[r - 1][c] == 1:
                labelMtx[r][c] = labelMtx[r-1][c]
            elif img[r][c - 1] == 1 and img[r - 1][c] == 1 and labelMtx[r][c-1] == labelMtx[r-1][c]:
                labelMtx[r][c] = labelMtx[r][c-1]
            elif img[r][c - 1] == 1 and img[r - 1][c] == 1 and labelMtx[r][c - 1] != labelMtx[r - 1][c]:
                minLabel = min(eqMtx[labelMtx[r][c-1]-1], eqMtx[labelMtx[r-1][c]-1])
                maxLabel = max(eqMtx[labelMtx[r][c-1]-1], eqMtx[labelMtx[r-1][c]-1])
                labelMtx[r][c] = minLabel
                for i in range(len(eqMtx)):
                    if eqMtx[i] == maxLabel:
                        eqMtx[i] = minLabel

print('Total Objects: ', np.count_nonzero(np.unique(eqMtx)))

