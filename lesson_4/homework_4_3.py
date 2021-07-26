'''
# Решение через while:
new_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dict_keys = list(new_dict.keys())
i = 0
while i < int(len(dict_keys)):
    new_key = dict_keys[i] + str(len(dict_keys[i]))
    new_dict[new_key] = new_dict.pop(dict_keys[i])
    i += 1
print(new_dict)'''
#решение через for:
new_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dict_keys = list(new_dict.keys())
for key in dict_keys:
    new_key = key + str(len(key))
    new_dict[new_key] = new_dict.pop(key)
print(new_dict)



