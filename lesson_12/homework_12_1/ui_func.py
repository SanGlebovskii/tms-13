"""Реализовать пользовательский
интерфейс с бесконечным циклом."""
from exceptions import *
from func import *


def calculate():
    while True:
        x = int(input('x = '))
        if not is_input_number_valid(x):
            print('Вы ввели не числовое значение.')
            continue
        sign = str(input('знак = '))
        if not is_operation_valid(sign):
            print('Вы ввели неправильный знак. Введите один из этих символов: +, -, *, /')
            continue

        y = int(input('y = '))
        if not is_input_number_valid(y):
            print('Вы ввели не числовое значение.')
            continue
        if is_divided_by_zero(y, sign):
            print('Деление на ноль запрещено')
            continue

        if sign == '+':
            result = add(x, y)
            print(result)

        if sign == '-':
            result = subtract(x, y)
            print(result)
        if sign == '*':
            result = multiply(x, y)
            print(result)

        if sign == '/':
            result = divide(x, y)
            print(result)
