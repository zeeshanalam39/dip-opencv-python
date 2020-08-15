import cv2 as cv
import numpy as np
from math import ceil

def createImage(w, h):
    img = np.zeros([w, h, 3], dtype=np.uint8)
    bw = ceil(w * 0.1)
    bh = ceil(h * 0.1)
    # First Method
    for i in range(0, w):
        for j in range(0, h):
            img[i][j] = 255
    # for i in range(0, w):
    #     for j in range(0, h):
    #         # Black
    #         if bw-i > 0:
    #             if bh-j > 0:
    #                 img[i][j] = (0, 0, 0)
    #         # Blue
    #
    #         # Red
    #         if i >= w-bw:
    #             if j >= h-bh:
    #                 img[i][j] = (1, 0, 0)
    # Second Method
    img[:bw, :bh] = (0, 0, 0)
    img[:bw, -bh:] = (255, 0, 0)
    img[-bw:, :bh] = (0, 255, 0)
    img[-bw:, -bh:] = (0, 0, 255)

    cv.imshow('Image', img)
    cv.waitKey(20000)
    cv.destroyAllWindows()

w = int(input('Enter width: '))
h = int(input('Enter height: '))
createImage(w, h)