class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def voice(self):
        print('Animal voice')


class Pet(Animal):
    def voice(self):
        print('Home animal voice')


class WildAnimal(Animal):
    def voice(self):
        print('Wild animal voice')


class Cat(Pet):
    def voice(self):
        print('Meow-meow')


class Dog(Pet):
    def voice(self):
        print('Woof-woof')


class Lion(WildAnimal):
    def voice(self):
        print('Arrr-arrrrrrr')


class Wolf(WildAnimal):
    def voice(self):
        print('Auuuuu-auuuuuuu')

cat = Cat(age=3, name='Cardi')
dog = Dog(age=8, name='Brungilda')
lion = Lion(age=6, name='Mufasa')
wolf = Wolf(age=14, name='Akella')
wolf.voice()
cat.voice()
dog.voice()
lion.voice()