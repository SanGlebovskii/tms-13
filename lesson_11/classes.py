"""Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и
площади окружности), Triangle(атрибуты: три точки, методы: нахождение
площади и периметра), Square(атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые
методы не описанные в задании. Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран[my-oop-03]
Примечание: в рамках задание создать два файла:  classes.py  и main.py. В
первом будут описаны все классы, во втором классы будут
импортированы и использованы."""
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Figure:
    def __init__(self, area=None, perimetr=None):
        self.area = area
        self.perimetr = perimetr

class Circle(Figure):
    def __init__(self, centre, len_radius):
        self.centre = centre
        self.len_radius = len_radius




class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def sides(self):
        x1 = self.a.x
        y1 = self.a.y
        x2 = self.b.x
        y2 = self.b.y
        x3 = self.c.x
        y3 = self.c.y

        ab = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        bc = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        ac = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        return ab, bc, ac
    def perimetr(self):
        ab, bc, ac = self.sides()
        result_perimetr = ab + bc + ac
        return result_perimetr
    def area(self):
        ab, bc, ac = self.sides()
        result_area = 0.5 * (bc + ac)
        return result_area

class Square(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b


