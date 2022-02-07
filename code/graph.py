# imports
import numpy as np
from tabulate import tabulate
from itertools import product

# array keeps hold of the lower matrix, later helps n conversion from binary to decimal
graph_array = []
# counter to check for already existing colour vector variations
# count = 0
# a list containing all the color vectors
cv_list = []
# result holds the value of the multiplication between the matrix and the colour vector
result = 0
next_color_vector = 0


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

# print the lower diagonal of the matrix multiplication
print("Lower triangular matrix: ")
lower(matrix, rows, cols)
print('\n')


def get_cv_list():
    counter = 0
    for vector in product([1, -1], repeat=5):
        # print(roll)
        cv_list.append(vector)
        counter = counter + 1
    print("There are {} number of colour vectors in the cv_list".format(counter))

    return cv_list


get_cv_list()
print(cv_list)

temp_list = []

# trial code
for i in range(len(cv_list)):
    temp_list.clear()
    count = 0
    # temp_list.append(cv_list[i])
    color_vector = np.array(cv_list[i])

    while True:  # change this with a while loop
        # color_vector = np.array(cv_list[j])
        result = np.matmul(matrix, color_vector)  # add a checker for 0 values here and it should replace
        # all the values to the prev colo_vector
        next_color_vector = np.sign(result).tolist()

        if next_color_vector not in temp_list:
            temp_list.append(next_color_vector)
            # color_vector = next_color_vector
            count = count + 1
            print("----------------        iteration {}         ---------------".format(count))
            print("The colour vector for this iteration is {}".format(color_vector))  # negative no -> -1
            print("The resulting 1x5 matrix is {}".format(result), '\n')
            print("The colour vector for the next iteration is {}".format(next_color_vector), '\n')
            print(temp_list)
        else:
            print("this already exists and the iteration loops on {} cycle".format(count))
            print("i increments by 1")
            break
print(temp_list)

table = [['graph number', 'no_of_vertices', 'loop', 'cycles', 'iteration_length'],
         [6, rows, 'yes', 0, 0],
         ['Mary', 'Jane', 25],
         ]
print(tabulate(table, headers='firstrow', tablefmt='grid'))

# look up into implying a lookup function which checks for the isomorphic graphs.
# looking up properties of graphs like clique and centrality based on the graph's
# adjacency matrix using a graph library in python
