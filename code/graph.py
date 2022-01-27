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
                # adds the lower matrix the graph_array list as a list of list.
                graph_array.append(Matrix[i][j])

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
graph_array = []
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

# # check for existing same variations
#             for x in range(j):
#                 if result not in temp_result:
#                     temp_result.append(result)
#                 else:
#                     print("This colour vector variation already exists!")
#
# for g in temp_result:
#     print(g)
# print the changed indices
# for x in updated_list:
#     print(x)

# rotating the list by 1 to the left so that the colour vector can be updated for
# 10 iterations eventually every time starting with a new color vector giving us a
# total of 100 results.(10*10)

# converts the lower matrix into a graph number
strings = [str(integer) for integer in graph_array]
graph_string = "".join(strings)
print(graph_string)


# converts the graph number from binary to normal
def convert_binary_to_decimal(graph_num_bin):
    decimal = 0
    for digit in graph_num_bin:
        decimal = decimal * 2 + int(digit)
    return decimal


# another way of converting the number to its binary form
print(convert_binary_to_decimal(graph_string))

# using the function to print the value
graph_num_in_dec = int(graph_string, 2)
# print(graph_num_in_dec)

# creating table
table = [['graph number', 'no_of_vertices', 'loop', 'cycles', 'iteration_length'],
         [graph_num_in_dec, rows, 'yes', 0, 0],
         ['Mary', 'Jane', 25],
         ]
print(tabulate(table, headers='firstrow', tablefmt='grid'))
