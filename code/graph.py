# imports
import numpy as np
from tabulate import tabulate
from itertools import product

# variables
# array keeps hold of the lower matrix, later helps n conversion from binary to decimal
graph_array = []
# counter to check for already existing colour vector variations
pi = 0
# a list containing all the color vectors
cv_list = []
# result holds the value of the multiplication between the matrix and the colour vector
result = 0
next_color_vector = 0
temp_list = []
# graph_list = [[1010011001], [0o110101100]]
n = int(input("Enter the number of vertices you want to do this for"))
N = int(1 / 2 * n * (n - 1))

print("The number of vertices you entered are {}".format(n))
print("N = {}".format(N))

# graph_list = [[[0, 0, 1, 0, 1],
#                [0, 0, 1, 1, 1],
#                [1, 1, 0, 0, 0],
#                [0, 1, 0, 0, 0],
#                [1, 1, 0, 0, 0]],
#               [[0, 1, 0, 0, 1],
#                [1, 0, 1, 0, 0],
#                [0, 1, 0, 1, 0],
#                [0, 0, 1, 0, 1],
#                [1, 0, 0, 1, 0]]
#               ]

graph_list = []
graph_int_list = []

zeroes = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

matrix = np.array([[0, 0, 1, 0, 1],
                   [0, 0, 1, 1, 1],
                   [1, 1, 0, 0, 0],
                   [0, 1, 0, 0, 0],
                   [1, 1, 0, 0, 0]])


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


# print the lower diagonal of the matrix multiplication
print("Lower triangular matrix: ")
lower(matrix, n, n)
print('\n')


def get_cv_list(rep):
    counter = 0
    for vector in product([1, -1], repeat=rep):
        # print(roll)
        cv_list.append(list(vector))
        counter = counter + 1
    print("There are {} number of colour vectors in the cv_list".format(counter))

    return cv_list


def get_graph_int_list(rep):
    counter = 0
    for graph in product([1, 0], repeat=rep):
        # print(roll)
        graph_int_list.append(list(graph))
        counter = counter + 1
    print("There total number of graphs are {}".format(counter))

    return graph_int_list


get_cv_list(n)
print(cv_list)

get_graph_int_list(N)
print(graph_int_list)


def convert_graph_list_to_matrix():
    counter = 0

    for k in graph_int_list:
        for i in range(len((1, n))):
            for j in range(len((0, i - 1))):
                zeroes[i][j] = k[i]

        graph_list.append(zeroes)

        counter = counter + 1

    print(counter)


convert_graph_list_to_matrix()
print(graph_list)

table = {'Graph number': ['Graph no.', 1],
         'Number of vertices': ['nov', 1],
         'starting colour vertex': ['Starting cv', 1],
         'ending colour vertex': ['Ending cv', 1],
         'loop': ['Loop', 1],
         'step time': ['Step time', 1],
         'cycle': ['Cycle', 1]
         }


# function that calculates the ending colour vector
# the cycle it loops on in case the iteration does go into a loop
def calculate_length_of_cycle():
    length = len(temp_list) - temp_list.index(next_color_vector)
    table['ending colour vertex'].append(next_color_vector)
    table['loop'].append('yes')
    table['step time'].append(length)


# function checking for 0s in the color_vector and replacing them with i of the previous color_vector
def check_for_zeroes(x):
    for k in range(len(x)):
        if x[k] == 0:
            x[k] = color_vector[k]


# try to optimize this function by reducing the time complexity


def convert_binary_to_decimal():
    strings = [str(integer) for integer in graph_array]
    graph_string = "".join(strings)
    # print("The graph number in binary is {}".format(graph_string))
    graph_num_in_dec = int(graph_string, 2)
    # print("The converted graph number from binary to decimal is {}".format(graph_num_in_dec))
    table['Graph number'].append(graph_num_in_dec)


def append_stuff_to_table():
    # graph table appends here
    # convert_binary_to_decimal()
    table['starting colour vertex'].append(cv_list[i])
    table['Number of vertices'].append(n)


# not trial code
for g in range(len(graph_list)):
    matrix = np.array(graph_list[g])
    pi = 0
    for i in range(len(cv_list)):
        pi = pi + 1
        # print("             Primary iteration {}            ".format(pi))
        temp_list.clear()
        count = 0
        color_vector = np.array(cv_list[i])
        append_stuff_to_table()

        while True:
            result = np.matmul(matrix, color_vector)
            next_color_vector = np.sign(result).tolist()
            if count == 0:
                temp_list.append(color_vector.tolist())
            check_for_zeroes(next_color_vector)

            if next_color_vector not in temp_list:
                temp_list.append(next_color_vector)
                count = count + 1
                # print("             Secondary iteration {}          ".format(count))
                # print("The colour vector for this iteration is {}".format(color_vector))  # negative no -> -1
                # print("The resulting 1x5 matrix is {}".format(result), '\n')
                color_vector = next_color_vector
                # print("The colour vector for the next iteration is {}".format(next_color_vector), '\n')
                # add an elif here to check if the program loops, whether it loops over 1 cv or a loop of
                # different ones to fill up the loop section of the table.

            else:
                # print("The colour vector iteration repeats here on this row {}".format(count))
                calculate_length_of_cycle()
                break

        # print("The temp_list is {}".format(temp_list))

table_data = tabulate(table, headers='firstrow', tablefmt='simple', showindex='always')
text_file = open("output.csv", "w")
text_file.write(table_data)
text_file.close()

# adjacency matrix using a graph library in python
# looking up properties of graphs like clique and centrality based on the graph's

# have a function which checks whether they are isomorphic and connected(should reduce the time complexity
# by skipping all teh non connected and te isomorphic ones
# Also can have a function which checks whether the iteration of this specific type
# has already been done before.

# and make a new column named cycle then which calculates if same vector repeats or oevr diff ones
