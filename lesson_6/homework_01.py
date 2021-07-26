from random import randint
n, m, a, b = int(input()), int(input()), int(input()), int(input())
maxi = a
matrix = []
for i in range(n):
    l = []
    for j in range(m):
        r = randint(a, b)
        l.append(r)
        if r > maxi:
            maxi = r
    matrix.append(l)
print(matrix)
print(maxi)