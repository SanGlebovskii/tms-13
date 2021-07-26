# Решение через while:
new_list = list(range(10))
i = 0
first_item = new_list[0]
while i < int(len(new_list)):
    if i == len(new_list) - 1:
        new_list[i] = first_item
    else:
        new_list[i] = new_list[i + 1]
    i += 1
print(new_list)
"""# Решение через for:
new_list = list(range(5))
first_item = new_list[0]
for i in range(len(new_list)):
    if i == len(new_list) - 1:
        new_list[i] = first_item
        break
    new_list[i] = new_list[i+1]
print(new_list)"""

