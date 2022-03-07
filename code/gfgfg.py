import numpy as np
k = [0, 1, 0, 1, 1, 0]

zeroes = []

n = int(input("enafdaj"))

# value_to_add = [[1, 1, 1, 1, 1, 1]]

zeros = [[0] * n for _ in range(n)]

counter = 0

for i in range(1, n):
    for j in range(0, i):
        zeros[i][j] = k[counter]
        counter = counter + 1
zeros = np.matrix(zeros)
zeros = zeros + np.matrix.transpose(zeros)
print(zeros)

