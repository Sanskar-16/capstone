# imports
import numpy as np
from tabulate import tabulate
from itertools import permutations


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

# for getting all the possible variations of the graph
possible_colour_vectors = {
    1: 1,
    2: 1,
    3: -1,
    4: -1,
    5: -1
}

perm = permutations(possible_colour_vectors.values())
cv_list = []

count = 0

for items in list(perm):
    if items in cv_list:
        continue
    else:
        cv_list.append(items)
        print(items)
        count += 1

print("There are {} umber of unique possible colour vectors.".format(count))

for i in range(len(cv_list)):
    color_vector = np.array(cv_list[i])
    result = np.matmul(matrix, color_vector)
    print("----------------------------------------------------")
    print("The resulting 1x5 matrix is {}".format(result), '\n')

# temp_array.append([-2, -3, 2, 1, 2])

# check for existing same variations

    for item in temp_array:
        if item in result:
            print("This variation already exists for row: {}".format(result[item]))
        else:
            temp_array.append(result)

    # Checks for
    for i in range(len(result)):
        if result[i] > 0:
            print("{}, Since the result is positive, it indicates there are more +1 edges for Row".format(result[i], i+1))
        elif result[i] < 0:
            print("{}, Since the result is negative, it indicates there are more -1 edges for Row".format(result[i], i+1))
        else:
            print("{}, Since the result is 0, it indicates the number of edges for both colours are same".format(result[i], i+1))

# expected result = [−2,−3,2,1,2]

# creating table
table = [['graph number', 'no_of_vertices', 'loop', 'cycles', 'iteration_length'],
         [12, 'John', 'Smith', 39], ['Mary', 'Jane', 25], ['Jennifer', 'Doe', 28]]
print(tabulate(table, headers='firstrow', tablefmt='grid'))
