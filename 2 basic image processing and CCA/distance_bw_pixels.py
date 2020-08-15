import numpy as np
import math as m

img = np.zeros([200, 200], dtype=np.uint8)
x1y1 = input("Input starting coordinates(x1,y1): ").split()
x1y1 = [int(i) for i in x1y1]
x2y2 = input("Input ending coordinates(x2,y2): ").split()
x2y2 = [int(i) for i in x2y2]
choice = int(input('Enter choice variable: '))

def distanceFunction(start, ending, choice):
    if choice == 1:
        distance = m.sqrt(pow((start[0] - ending[0]), 2) + pow((start[1] - ending[1]), 2))
        print('Euclidean Distance is = ', "%.2f" % distance)
    elif choice == 2:
        distance = abs(start[0] - ending[0]) + abs(start[1] - ending[1])
        print('City Block Distance is = ', "%.2f" % distance)
    else:
        distance = max(abs(start[0] - ending[0]), abs(start[1] - ending[1]))
        print('Chessboard Distance is = ', "%.2f" % distance)


distanceFunction(x1y1, x2y2, choice)