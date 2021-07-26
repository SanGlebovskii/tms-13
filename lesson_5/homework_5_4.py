n = int(input())


def sum_of_n(number) -> int:
    summary = 0
    for i in range(1, number + 1):
        summary += 1 / i
    return summary


print(sum_of_n(n))
