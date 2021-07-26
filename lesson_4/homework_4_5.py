"""
# Решение через for:
new_list = [1, 1]
for i in range(15-2):
    sum = new_list[i] + new_list[i + 1]
    new_list.append(sum)
print(new_list)"""
# Решение через while:
import sys
number_elements = int()
try:
    number_elements = int(input('количество элементов чисел Фибоначчи'))
except:
    print('Вы ввели не числовое значение, попробуйте еще раз')
    sys.exit()
new_list = [1, 1]
i = 0
while i < number_elements - 2:
    sum = new_list[i] + new_list[i + 1]
    new_list.append(sum)
    i += 1
print(new_list)
