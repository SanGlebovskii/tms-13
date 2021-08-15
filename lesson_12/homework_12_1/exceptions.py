"""Добавить валидацию входных данных."""


def is_operation_valid(sign) -> bool:
    if sign != '+' and sign != '-' and sign != '*' and sign != '/':
        return False
    else:
        return True


def is_input_number_valid(number) -> bool:
    if type(number) != int:
        return False
    else:
        return True


def is_divided_by_zero(number, sign) -> bool:
    if sign == '/' and number == 0:
        return True
    else:
        return False
