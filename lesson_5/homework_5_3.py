def sum_of_divisors(a) -> int:
    s = 0
    for i in range(1, a):
        if a % i == 0:
            s += i
    return s


def amicable_numbers(start_number, end_number) -> list:
    result = []
    for i in range(start_number, end_number + 1):
        if i not in result:
            summary = sum_of_divisors(i)
            if i == sum_of_divisors(summary) and i != summary:
                result.append(i)
                result.append(summary)
    return result


print(amicable_numbers(200, 300))
