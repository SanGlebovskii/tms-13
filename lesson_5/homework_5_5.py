from random import randint
new_list = [randint(1, 800) for i in range(19)]
print(new_list)
max_element = max(new_list)
for i in range(len(new_list)):
    if new_list[i] % 2 == 0:
        new_list[i] = max_element
print(new_list)
