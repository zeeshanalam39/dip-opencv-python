x = [[1, 2, 3, 4, 5], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35]]
print(x[1][3:5])
print(x[0][2:4])
print(x[2][1:2])
print(x[1][0:5:2])

y = [0, 0, 0]
for i in range(3):
    y[i] = sum(x[i])/len(x[i])

print(y)

# i = 0
# j = 0
# sum = 0
# while i < len(x):
#     sum = j = 0
#     while j < len(x[i]):
#         sum = sum + x[i][j]
#         j = j+1
#     y[i] = sum/len(x[i])
#     i = i+1

# print(y)