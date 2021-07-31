"""last_words = 'привет как дела'
new_list = last_words.split()
reverse_words = [i[::-1] for i in new_list]
print(' '.join(reverse_words))"""
dict_students = [
    {
    'name': 'John Smit',
    'math': 10,
    'phys': 9,
    'chem': 6,
}
]
"""dict_students.update(dict([(key, item) for item, key in dict_students.items()[:2] if item in [1, 2]]))
print(dict_students)"""
dict_1 = {'aa':1, 'bb':2, 'ss':3}
d = {value: key for key, value in dict_1.items()}

#for key, value in dict_1.items():
   #d[value] = key
print(d)