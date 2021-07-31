new_list = [3, 6, 9, 4, 5]


def double_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * double_factorial(n - 2)


for element in new_list:
    print(double_factorial(element))
