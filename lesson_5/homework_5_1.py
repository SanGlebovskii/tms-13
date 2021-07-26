while True:
    x = int(input('x = '))
    y = int(input('y = '))
    sign = str(input('знак = '))
    global z
    if sign == '0':
        break
    if sign not in ('+', '-', '/', '*'):
        continue
    if sign == '+':
        z = x + y
        print(z)
    elif sign == '-':
        z = x - y
        print(z)
    elif sign == '*':
        z = x * y
        print(z)
    elif sign == '/':
        if y != 0:
            z = x / y
            print(z)
        else:
            print('На ноль делить нельзя!')





