class Cat:
    def __init__(self, name, age, weight, height, master, adress):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height
        self.__master = master
        self.__adress = adress
    def meow(self):
        print('Meow-meow')
    def satan_party(self):
        print('AAAA, jump-jump, MEOOOOW, MEoooooooWWW')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, adress):
        self.__adress = adress

cat = Cat(name='Cardi', age=4, weight=3.5, height=70, master='Gleb', adress='Grodno')
print(cat.age)
class Flat:
    def __init__(self, room, master, square):
        self.__room = room
        self.__master = master
        self.__square = square
    def rent(self, rent):
        rent = 120 * 2.54
        print('Нужно заплатить ', rent, ' б.р')
    def harvesting(self):
        print('Грязно. Пора убирать')

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, room):
        self.__room = room

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, square):
        self.__square = square
flat = Flat(room=1, master='Gleb', square= 45)
print(flat.master)
class Friend:
    def __init__(self, name, age, adress):
        self.__name = name
        self.__age = age
        self.__adress = adress
    def help(self):
        print('Always, bro')
    def party(self):
        print('Yehuuu')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, adress):
        self.__adress = adress
friend = Friend(name='Vladislav', age=26, adress='Lida')
print(friend.party())
class Computer:
    def __init__(self, name, os, year):
        self.__name = name
        self.__os = os
        self.__year = year
    def include(self):
        print('Press "On"')
    def turn_off(self):
        print('Press "Off"')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def os(self):
        return self.__os

    @os.setter
    def adress(self, os):
        self.__os = os

    @property
    def year(self):
        return self.__year

    @year.setter
    def adress(self, year):
        self.__year = year
computer = Computer(name='Lenovo', os='Windows', year='2016')
print(computer.os)
class Planet:
    def __init__(self, name, dimensions, galaxy):
        self.__name = name
        self.__dimensions = dimensions
        self.__galaxy = galaxy
    def apocalipsis(self):
        print('The End')
    def alien_invasion(self):
        print('Wathing "Independence Day"')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        self.__dimensions = dimensions

    @property
    def galaxy(self):
        return self.__galaxy

    @galaxy.setter
    def galaxy(self, galaxy):
        self.__galaxy = galaxy
planet = Planet(name='Earth', dimensions='small', galaxy='Milky Way')
print(planet.name, planet.galaxy)
