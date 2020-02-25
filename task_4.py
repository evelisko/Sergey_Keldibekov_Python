# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


from enum import Enum
from user_functions import float_convert


class Trun(Enum):
    left = 1
    rigth = 2
    none = 3


class Car(object):
    car_type = 'Custom'
    speed_limit = None

    def __init__(self, name, color):
        self._speed = 0.0
        self._color = color
        self._name = name
        self._turn = Trun.none
        self._is_police = False

    def __str__(self):
        return f'{self.car_type} {self._name} {self._color}'

    def go(self, speed):
        speed = float_convert(speed)
        if speed != -1:
            self._speed = speed

    def stop(self):
        self._speed = 0.0
        self._turn = Trun.none

    def turn(self, truning=Trun.none):
        self._turn = truning

    def show_speed(self):
        if self.speed_limit and self._speed > self.speed_limit:
            print('Вы превысили скорость', end=' ')
        return self._speed


class SportCar(Car):
    car_type = 'SportCar'

class TownCar(Car):
    car_type = 'TownCar'
    speed_limit = 60

    # def show_speed(self):
    #     if self._speed > speed_limit:
    #         print(f'{self._speed} Вы превысили скорость', end=' ')
    #     return super(TownCar, self).show_speed()


class WorkCar(Car):
    car_type = 'WorkCar'
    speed_limit = 40

    # def show_speed(self):
    #     if self._speed > 40:
    #         print('Вы превысили скорость', end=' ')
    #     return self._speed


class PoliceCar(Car):
    car_type = 'PoliceCar'

    def __init__(self, name, color):
        super().__init__(name, color)
        self._is_police = True


car_1 = SportCar(name='Ferrary', color='Red')
car_2 = WorkCar(name='Ford', color='Brown')
car_3 = TownCar(name='Fiat', color='White')
car_4 = PoliceCar(name='Ford', color='White/Black')

car_1.go(170)
car_2.go(60)
car_3.go(60)
car_4.go(70)
print('Поехали')
print(car_1, car_1.show_speed())
print(car_2, car_2.show_speed())
print(car_3, car_3.show_speed())
print(car_4, car_4.show_speed())

car_1.stop()
car_2.stop()
car_3.stop()
car_4.stop()
print()
print('Автомобили остановились')

print(car_1, car_1.show_speed())
print(car_2, car_2.show_speed())
print(car_3, car_3.show_speed())
print(car_4, car_4.show_speed())
