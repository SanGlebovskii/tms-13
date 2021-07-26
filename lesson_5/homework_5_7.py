from random import randint

n = 6
m = 6
matrix_one = []
for i in range(n):
    matrix_second = []
    for j in range(m):
        matrix_second.append(randint(1, 9))
    matrix_one.append(matrix_second)
print(matrix_one)
for i in range(len(matrix_one)):
    max_element = max(matrix_one[i])
    matrix_one[i][i] = max_element
print(matrix_one)
