# imports
import numpy as np
from tabulate import tabulate
from itertools import product


# array keeps hold of the lower matrix, later helps n conversion from binary to decimal
graph_array = []
# counter to check for already existing colour vector variations
count = 0
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

#
# def get_cv_list():
#     counter = 0
#     for vector in product([1, -1], repeat=5):
#         # print(roll)
#         cv_list.append(vector)
#         counter = counter + 1
#     print("There are {} number of colour vectors in the cv_list".format(counter))
#
#     return cv_list
#
#
# get_cv_list()

# function for generating the colour vector list
cv_list.append([1, 1, -1, -1, -1])

# converts the lower matrix into a graph number
strings = [str(integer) for integer in graph_array]
graph_string = "".join(strings)
print("The graph number in binary is {}".format(graph_string))

# # converts the graph number from binary to normal
# def convert_binary_to_decimal(graph_num_bin):
#     decimal = 0
#     for digit in graph_num_bin:
#         decimal = decimal * 2 + int(digit)
#     return decimal
#
#
# # using the function to print the value of the binary number in decimal
# print(convert_binary_to_decimal(graph_string))

# another way of converting the number to its binary form using the int() function
graph_num_in_dec = int(graph_string, 2)
print("The converted graph number from binary to decimal is {}".format(graph_num_in_dec))

# creating table
table = [['graph number', 'no_of_vertices', 'loop', 'cycles', 'iteration_length'],
         [graph_num_in_dec, rows, 'yes', 0, 0],
         ['Mary', 'Jane', 25],
         ]
print(tabulate(table, headers='firstrow', tablefmt='grid'))

# trial code
for i in range(len(cv_list)):
    for j in range(len(cv_list) + 2):
        color_vector = np.array(cv_list[j])
        result = np.matmul(matrix, color_vector)
        next_color_vector = np.sign(result).tolist()
        cv_list.append(next_color_vector)
        count = count + 1
        print("----------------        iteration {}         ---------------".format(count))
        print("The colour vector for this iteration is {}".format(color_vector))  # negative no -> -1
        print("The resulting 1x5 matrix is {}".format(result), '\n')
        print("The colour vector for the next iteration is {}".format(next_color_vector), '\n')

# try to make most of the code fucntion based.
