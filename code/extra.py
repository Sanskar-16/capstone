# import numpy as np
#
# matrix = np.array([[0, 0, 1, 0, 1],
#                    [0, 0, 1, 1, 1],
#                    [1, 1, 0, 0, 0],
#                    [0, 1, 0, 0, 0],
#                    [1, 1, 0, 0, 0]])
# graph_array = []
# n = 5
#
#
# # function to print the lower diagonal
# def lower(Matrix, row, col):
#     for i in range(0, row):
#         for j in range(0, col):
#             if i == j:
#                 print("0", end=" ")
#             elif i < j:
#                 print(" ", end=" ")
#             else:
#                 print(Matrix[i][j],
#                       end=" ")
#                 # adds the lower matrix the graph_array list as a list of list.
#                 graph_array.append(Matrix[i][j])
#
#         print(" ")
#
#
# # print the lower diagonal of the matrix multiplication
# print("Lower triangular matrix: ")
# lower(matrix, n, n)
# print('\n')
# from itertools import product
# cvllist = []
# cv_list = []
#
#
# def get_cv_list(rep):
#     counter = 0
#     for vector in product([1, -1], repeat=rep):
#         cvllist.append(list(vector))
#         cvllist[counter].insert(0, 1)
#         counter = counter + 1
#     print("There are {} number of colour vectors in the cv_list".format(counter))
#
#     return cvllist
#
# def get_cv_listt(rep):
#     counter = 0
#     for vector in product([1, -1], repeat=rep):
#         # print(roll)
#         cv_list.append(list(vector))
#         counter = counter + 1
#     print("There are {} number of colour vectors in the cv_list".format(counter))
#
#     return cv_list
#
#
# get_cv_list(4)
# get_cv_listt(5)
#
# print(cvllist)
# print(cv_list)
#
#
# CONVERTING GRAPH BIT STRINGS TO MATRICES
# import numpy as np
# k = [0, 1, 0, 1, 1, 0]
#
# n = int(input("enafdaj"))
#
# zeros = [[0] * n for _ in range(n)]
#
# counter = 0
#
# for i in range(1, n):
#     for j in range(0, i):
#         zeros[i][j] = k[counter]
#         counter = counter + 1
#
# zeros = np.matrix(zeros)
# zeros = zeros + np.matrix.transpose(zeros)
# print(zeros)
