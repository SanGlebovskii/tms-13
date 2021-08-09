class Car:
    def __init__(self, brand, model, year, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed
    def increase_speed(self):
        return self.__speed + 5
    def reduce_speed(self):
        return self.__speed - 5
    def stop_car(self):
        self.__speed = 0
        return self.__speed
    def speedometr(self):
        print(self.__speed)
    def u_turn(self):
        return -self.__speed
car = Car(brand='BMW', model='M4', year='2017', speed=250)
print(car.increase_speed())
