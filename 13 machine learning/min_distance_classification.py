import numpy as np  # Importing packages
import pandas as pd
from sklearn.model_selection import train_test_split

CSV_PATH = 'D:\@Semester 06\Digital Image Processing\Lab\Manuals\Figures\lab13\data.csv'    # CSV File Path
dataset = pd.read_csv(CSV_PATH)     # Reading dataset file

Class1 = dataset.iloc[0:50, :].values   # Class 1 output
Class2 = dataset.iloc[51:100, :].values     # Class 2 output

Train, test = train_test_split(dataset, test_size=0.20, random_state=0)     # Sepearting train & test data
test = test.iloc[:, :-1].values

# Finding mean of each attribute of each class
Mean_List1 = Mean_List2 = []

for i in range(4):
    m1 = np.mean(Class1[:, i])
    m2 = np.mean(Class2[:, i])
    Mean_List1.append(m1)
    Mean_List2.append(m2)

#   Finding Distances
for index in range(len(test)):
    values = test[index]
    distance1 = np.sqrt(
        ((values[0] - Mean_List1[0]) ** 2) + ((values[1] - Mean_List1[1]) ** 2) + ((values[2] - Mean_List1[2]) ** 2) + (
                (values[3] - Mean_List1[3]) ** 2))
    distance2 = np.sqrt(((values[0] - Mean_List2[0]) ** 2) + ((values[1] - Mean_List2[1]) ** 2) + ((values[2] -Mean_List2[2]) ** 2) + ((values[3] - Mean_List2[3]) ** 2))
    print('Distance of test point from class 1(Iris-setosa) is', distance1)
    print('Distance of test point from class 2(Iris-versicolor) is', distance2)
    if distance1 > distance2:
        print('Test point', values, 'belong to Iris-versicolor\n')
    else:
        print('Test point', values, 'belong to Iris-setosa\n')