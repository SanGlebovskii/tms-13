"""
#Решение через while:
new_list = list(range(20))
i = 0
count = 0
while i < int(len(new_list)):
    if int(new_list[i])%2 == 0:
        count += 1
    i += 1
print(count)"""
# Решение через for:
second_list = list(range(100))
second_count = 0
for i in second_list:
    if int(i % 2) == 0:
        second_count += 1
print(second_count)
