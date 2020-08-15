# Credits: Talha Khursheed Qazi

import csv      # Importing packages
from scipy.spatial import distance
import numpy as np
import random


def read_dataset(link):     # Read dataset file
    my_list = []
    with open(link, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            my_list.append(row)
    my_list.pop(0)
    data = np.array(my_list)    # Convert list to np array
    return data


def calculate_distance(x, flower1, flower):
    counter = 0
    dist_list = []
    for y in flower1:
        if counter < 80:
            distance0 = distance.euclidean(x, y)
            dist_list.append((distance0, flower[counter][4]))
        counter = counter + 1
    return dist_list


def find_neighbours(k, dist_list):
    new_list = []
    counter = 0
    for x in dist_list:
        new_list.append(x)
        counter = counter + 1
        if counter == k:
            break
    return new_list


def get_response(new_list):
    class0 = class1 = 0
    for x in new_list:
        if x[1] == 0.0:
            class0 = class0 + 1
        else:
            class1 = class1 + 1
        if class0 > class1:
            label = 0
        else:
            label = 1
    return label


CSV_PATH = 'D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab13\data.csv'    # CSV File Path
data = read_dataset(CSV_PATH)
# binary Classification
for x in range(100):
    if x < 50:
        data[x][4] = 0
    else:
        data[x][4] = 1
flower = data.tolist()
# shuffling the rows
random.shuffle(flower)
flower = np.array(flower)
flower = flower.astype(np.float)
flower1 = flower[:, 0:4]
unseen_smaple1 = [14.0, 14.5, 12.0, 12.5]
unseen_smaple2 = [22, 21, 3, 26]
unseen_smaple3 = [2.0, 0.5, 1.2, 2.6]
unseen_smaple = [unseen_smaple1, unseen_smaple2, unseen_smaple3]
result = []
for x in unseen_smaple:
    dist_list = calculate_distance(x, flower1, flower)
    dist_list.sort()
    new_list = find_neighbours(5, dist_list)
    label = get_response(new_list)
    result.append(label)

for i in result:
    if i == 0:
        print('Sample belongs to versicolor')
    else:
        print('Sample belongs to setosa')
# Accuracy code
data = read_dataset(CSV_PATH)
# binary Classification
for x in range(100):
    if x < 50:
        data[x][4] = 0
    else:
        data[x][4] = 1
flower = data.tolist()
# shuffling the rows
random.shuffle(flower)
flower = np.array(flower)
flower = flower.astype(np.float)
flower1 = flower[:, 0:4]
counter = 0
true_guess = 0
for x in flower1:
    if counter >= 80:
        dist_list = calculate_distance(x, flower1, flower)
        dist_list.sort()
        new_list = find_neighbours(5, dist_list)
        label = get_response(new_list)
        if label == flower[counter][4]:
            true_guess = true_guess + 1
    counter = counter + 1
accuracy = (true_guess / 20) * 100

print('Accuracy is:', accuracy)
