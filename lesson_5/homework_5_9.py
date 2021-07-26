m, n = int(input()), int(input())
for i in range(m, n + 1):
    res = []
    for j in range(2, i):
        if i % j == 0:
            res.append(j)
    print(str(i) + ':', *res)