"""Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени( 12:65:83 - 13:06:23)"""


class MyTime:
    def __init__(self, str_time=None, mytime_obj=None, hours=0, minutes=0, seconds=0):
        if str_time:
            str_time.split(":")
        elif mytime_obj:
            self.hours = mytime_obj.hours
            self.minutes = mytime_obj.minutes
            self.seconds = mytime_obj.seconds

        else:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
            if self.minutes > 60:
                self.hours += 1
            if self.seconds > 60:
                self.minutes += 1

    def __add__(self, arg):
        h = self.hours + arg.hours
        m = self.minutes + arg.minutes
        s = self.seconds + arg.seconds
        return MyTime(hours=h, minutes=m, seconds=s)

    def __eq__(self, arg):
        return (self.hours == arg.hours) and (self.minutes == arg.minutes) and (self.seconds == arg.seconds)

    def __ne__(self, arg):
        return (self.hours != arg.hours) or (self.minutes != arg.minutes) or (self.seconds != arg.seconds)

    def __sub__(self, arg):
        self.hours -= arg.hours
        self.minutes -= arg.minutes
        self.seconds -= arg.seconds
        return self

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'
    def __lt__(self, arg):
        if self.hours < arg.hours:
            return True
        if self.hours > arg.hours:
            return False
        if self.minutes < arg.minutes:
            return True
        if self.minutes > arg.minutes:
            return False
        if self.seconds < arg.seconds:
            return True
        if self.seconds > arg.seconds:
            return False

    def __gt__(self, arg):
        if self.hours > arg.hours:
            return True
        if self.hours < arg.hours:
            return False
        if self.minutes > arg.minutes:
            return True
        if self.minutes < arg.minutes:
            return False
        if self.seconds > arg.seconds:
            return True
        if self.seconds < arg.seconds:
            return False

    def __le__(self, arg):
        if self.hours <= arg.hours:
            return True
        if self.hours > arg.hours:
            return False
        if self.minutes <= arg.minutes:
            return True
        if self.minutes > arg.minutes:
            return False
        if self.seconds <= arg.seconds:
            return True
        if self.seconds > arg.seconds:
            return False

    def __ge__(self, arg):
        if self.hours >= arg.hours:
            return True
        if self.hours < arg.hours:
            return False
        if self.minutes >= arg.minutes:
            return True
        if self.minutes < arg.minutes:
            return False
        if self.seconds >= arg.seconds:
            return True
        if self.seconds < arg.seconds:
            return False



obj_1 = MyTime(hours=22, minutes=24, seconds=1)
obj_2 = MyTime(hours=21, minutes=35, seconds=1)
# print(obj_1 != obj_2)
result = obj_2 <= obj_1
# result_2 = obj_1 + obj_2
print(result)
# print(result_2)
