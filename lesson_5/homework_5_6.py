from random import randint

new_list = [randint(-10, 10) for i in range(15)]
print(new_list)


def list_count(array) -> int:
    count = 0
    flag = False
    for i in range(len(new_list) - 1):
        if new_list[i] < new_list[i + 1]:
            flag = True
            continue
        elif flag:
            count += 1
            flag = False
        if len(new_list) == i + 1 and flag == True:
            count += 1

    return count


print(list_count(new_list))
