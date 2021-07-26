"""high_in_metres = [2700, 3200, 6400, 11000, 39000]
high_in_fut = list(map(lambda x: x * 0.3048, high_in_metres))
print(high_in_fut)
dict_students = [
    {
    'name': 'John Smit',
    'math': 10,
    'phys': 9,
    'chem': 6,
},
{
    'name': 'Buba Smit',
    'math': 8,
    'phys': 9,
    'chem': 4,
},

{
    'name': 'Carl Johnson',
    'math': 6,
    'phys': 7,
    'chem': 10,
}

]

list_students = list(map(lambda dict_students.items[1])
print(list_students)"""
import numpy
list_numbers = list(range(-20, 20))
a = numpy.mean(list_numbers)
new_list = list(filter(lambda x: x > a, list_numbers))
print(new_list)

