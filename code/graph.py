import numpy as np


# function to print the lower diagonal
def lower(Matrix, row, col):
    for i in range(0, row):
        for j in range(0, col):
            if i == j:
                print("0", end=" ")
            elif i < j:
                print(" ", end=" ")
            else:
                print(Matrix[i][j],
                      end=" ")

        print(" ")


matrix = np.array([[0, 0, 1, 0, 1],
                  [0, 0, 1, 1, 1],
                  [1, 1, 0, 0, 0],
                  [0, 1, 0, 0, 0],
                  [1, 1, 0, 0, 0]])

rows = 5
cols = 5

temp_array = []

print("Lower triangular matrix: ")
lower(matrix, rows, cols)
print('\n')

color_vertex = np.array([1, 1, -1, -1, -1])
print(bin(5))


result = np.matmul(matrix, color_vertex)
print("The resulting 1x5 matrix is {}".format(result), '\n')

temp_array.append([-2, -3, 2, 1, 2])

# check for existing same variations
for item in temp_array:
    if item in result:
        print("This variation already exists for row: {}".format(result[item]))
    else:
        temp_array.append(result)

# Checks for
for i in range(len(result)):
    if result[i] > 0:
        print("{}, Since the result is positive, it indicates there are more +1 edges for Row".format(result[i], i + 1),
              '\n')
    elif result[i] < 0:
        print("{}, Since the result is negative, it indicates there are more -1 edges for Row".format(result[i], i + 1),
              '\n')
    else:
        print("{}, Since the result is 0, it indicates the number of edges for both colours are same".format(result[i],
                                                                                                             '\n'),
              i + 1)

# expected result = [−2,−3,2,1,2]
