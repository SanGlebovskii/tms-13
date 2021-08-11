from classes import *

figures = []
figures.append(Triangle(Point(5, 2), Point(4, 4), Point(1, 9)))
figures.append(Circle(Point(10, 2), r=5))
figures.append(Square(Point(10, 2), Point(5, 2)))
for i in figures:
    print(i.perimetr())
