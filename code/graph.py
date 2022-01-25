# imports
import numpy as np
from tabulate import tabulate
from itertools import permutations
import collections


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

temp_result = []
cv_list = []
count = 0

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

# temp_result.append([0, -1, 0, -1, 0])

for item in list(perm):
    if item in cv_list:
        continue
    else:
        cv_list.append(item)
        print(item)
        count += 1
print("There are {} umber of unique possible colour vectors.".format(count))


# gives out the values for every iteration for every colour vector(10*10*5)
for k in range(len(cv_list)):
    for i in range(len(cv_list)):
        color_vector = np.array(cv_list[i])
        result = np.matmul(matrix, color_vector)
        print("----------------------------------------------------")
        print("The colour vector for this iteration is {}".format(color_vector))
        print("The resulting 1x5 matrix is {}".format(result), '\n')

        # # check for existing same variations
        # for x in range(len(temp_result)):
        #     if result not in temp_result:
        #         temp_result.append(result)
        #     else:
        #         print("This colour vector variation already exists!")

        # Checks for the dominant kind of edges.
        for j in range(len(result)):
            if result[j] > 0:
                print("{}, Since the result is positive, it indicates there are more +1 edges for Row".format(result[j],
                                                                                                              i + 1))
            elif result[j] < 0:
                print("{}, Since the result is negative, it indicates there are more -1 edges for Row".format(result[j],
                                                                                                              i + 1))
            else:
                print("{}, Since the result is 0, it indicates the number of edges for both colours are same".format(
                    result[j], j + 1))

    # pushes the list indices by 1, creating a new colour vector every iteration
    temp_list = collections.deque(cv_list)
    temp_list.rotate(-1)
    updated_list = list(temp_list)
    cv_list = updated_list
    print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x", '\n')

# print the changed indices
# for x in updated_list:
#     print(x)

# rotating the list by 1 to the left so that the colour vector can be updated for
# 10 iterations eventually every time starting with a new color vector giving us a
# total of 100 results.(10*10)


# # creating table
# table = [['graph number', 'no_of_vertices', 'loop', 'cycles', 'iteration_length'],
#          [12, 'John', 'Smith', 39], ['Mary', 'Jane', 25], ['Jennifer', 'Doe', 28]]
# print(tabulate(table, headers='firstrow', tablefmt='grid'))