import cv2 as cv
import numpy as np

IMAGE = cv.imread('D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab8\_img.bmp', 0)  # Read Img
cv.imshow('Original Image', IMAGE)
cv.waitKey(0)
cv.destroyAllWindows()


def kMeansClustering(img, k):
    size = np.shape(img)    # Get img shape
    rows = size[0]
    cols = size[1]
    meanC1 = 4
    meanC2 = 70
    cluster1 = []       # Lists to store clusters
    cluster2 = []
    for r in range(rows):   # Create initial clusters
        for c in range(cols):
            if abs(img[r][c]-meanC1) < abs(img[r][c]-meanC2):
                cluster1.append(img[r][c])
            else:
                cluster2.append(img[r][c])

    meanC1 = sum(cluster1)/len(cluster1)    # Find mean of clusters
    meanC2 = sum(cluster2)/len(cluster2)
    while abs(meanC1) != abs(meanC2):       # Go in loop until both means become equal
        for r in range(len(cluster1)):
            if abs(cluster1[r] - meanC1) < abs(cluster1[r] - meanC2):
                # cluster1.append(img[r][c])
                print('This value remains intact in cluster1')
            else:
                cluster2.append(img[r][c])

        for r in range(len(cluster2)):
            if abs(cluster2[r] - meanC1) < abs(cluster2[r] - meanC2):
                # cluster1.append(img[r][c])
                print('This value remains intact in cluster2')
            else:
                cluster1.append(img[r][c])

        meanC1 = sum(cluster1) / len(cluster1)
        meanC2 = sum(cluster2) / len(cluster2)

    for r in range(rows):       # Segment image based on final means
        for c in range(cols):
            if abs(img[r][c]-meanC1) < abs(img[r][c]-meanC2):
                img[r][c] = meanC1
            else:
                img[r][c] = meanC2

    cv.imshow('K Means Clustering', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


kMeansClustering(IMAGE, 2)    # Call function
