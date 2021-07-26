a = int(input())
summ = 0
ext = 1
while a > 0:
    summ += a % 10
    ext *= a % 10
    a = a // 10
print(summ)
print(ext)

