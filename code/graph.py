# imports
import numpy as np
import pandas as pd
from itertools import product
import networkx as nx
import time

# starting the time for which the program shall run
start_time = time.time()

# declaring all the essential variables and data structures
graph_array = []
pi = 0
cv_list = []
result = 0
next_color_vector = 0
graph_no = 0
temp_list = []
graph_list = []
graph_int_list = []
zero = [[]]

# a dictionary which holds the value for all the variables before and after computations
table = {'Graph number': [],
         'Number of vertices': [],
         'starting colour vertex': [],
         'ending colour vertex': [],
         'loop': [],
         'cycle': [],
         'step time': []
         }


# function that creates the required zero matrix on user input
def get_zero_matrix(x):
    global zero
    zero = [[0] * x for _ in range(x)]
    print("The zero matrix for {} vertices is {}".format(x, zero))


# function to get the list of all possible colour vectors
def get_cv_list(rep):
    counter = 0
    for vector in product([1, -1], repeat=rep - 1):
        cv_list.append(list(vector))
        cv_list[counter].insert(0, 1)
        counter = counter + 1
    print("There are {} colour vectors in total for {} vertices".format(counter, n))
    print(cv_list)
    print('\n')

    return cv_list


# function to get the list of all possible graphs
def get_graph_int_list(rep):
    counter = 0
    for graph in product([1, 0], repeat=rep):
        graph_int_list.append(list(graph))
        counter = counter + 1
    print("There are {} graphs in total for {} vertices".format(counter, n))
    print(graph_int_list)
    print('\n')

    return graph_int_list


# checks whether the graph passed as a parameter is connected or not
def check_connected(x):
    for _ in x:
        if nx.is_connected(x):
            continue
        else:
            break


# function checking for 0s in the color_vector and replacing them with i of the previous color_vector
def check_for_zeroes(x):
    for k in range(len(x)):
        if x[k] == 0:
            x[k] = color_vector[k]


'''
step calculates the number of steps it takes for the algorithm to reach the same vector after it starts looping a
vector, if the algorithm loops on the same vector, it will show 1. Otherwise, step would be number of vectors between
the starting loop vector and when it occurs again.

whereas the length var, it calculates the number of steps it takes for teh algorithm to reach teh starting
colour vector again in the colour vector list.
'''


# function that calculates and appends the values for 'step time' and 'cycle' to the dictionary
def calculate_length_of_cycle():
    step = len(temp_list) - temp_list.index(next_color_vector)
    length = temp_list.index(next_color_vector) + 1
    table['ending colour vertex'].append(next_color_vector)
    table['loop'].append('yes')
    table['step time'].append(step)
    table['cycle'].append(length)


# another append function for adding rest of the components of the algorithm to the dictionary
def append_stuff_to_table():
    # graph table appends here
    # convert_binary_to_decimal()
    table['starting colour vertex'].append(cv_list[i])
    table['Number of vertices'].append(n)
    table['Graph number'].append(graph_no)


# taking input from the user
n = int(input("Enter the number of vertices you want to do this for - "))
N = int(1 / 2 * n * (n - 1))

# obtaining all the essential lists based on user input
print("The number of vertices (n) is {} which implies n bit binary string (N) is {}".format(n, N))
get_zero_matrix(n)
get_graph_int_list(N)
get_cv_list(n)

# main algorithm
for g in graph_int_list:
    zeroes = zero
    graph_counter = 0
    for i in range(1, n):
        for j in range(0, i):
            zeroes[i][j] = g[graph_counter]
            graph_counter = graph_counter + 1

    zeroes = np.matrix(zeroes)
    zeroes = zeroes + np.matrix.transpose(zeroes)
    print(zeroes)
    matrix = np.array(zeroes)
    G = nx.from_numpy_matrix(matrix)
    graph_no = graph_no + 1
    if nx.is_connected(G):
        print("this graph is connected...")
        for i in range(len(cv_list)):
            pi = pi + 1
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
                    color_vector = next_color_vector

                else:
                    calculate_length_of_cycle()
                    break
    else:
        print("skipped this graph, because it is not connected.")

# converting all the computations in a tabular format
df = pd.DataFrame(table)
df.to_csv('..\\output\\output.csv', index_label=False)

# calculating and printing the total time it took to run the program
print("Program completed")
print("--- %s seconds ---" % (time.time() - start_time))
# adjacency matrix using a graph library in python
# looking up properties of graphs like clique and centrality based on the graph's
# run for 7/8 and look for a loop bigger than 2
# data analysis on loop size and other properties for all the graphs(percent of all the loop size 1 graphs)
# insights from teh above analysis
# majority from colour 1 to colour 2
# cycle - no of rows DONE
# look for a dataset on which it could be implemented
# include what else could have been added to the report
