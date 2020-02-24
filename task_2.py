# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

from user_functions import float_convert


class Road(object):

    def __init__(self, length, width, height=5, specific_massa=25):
        self._length = length
        self._width = width
        self._heigth = height
        self._specific_massa = specific_massa

    def set_heigth(self, height):
        self._heigth = float_convert(height)
        if self._heigth == -1:
            self._heigth = 5

    def set_specific_massa(self, massa):
        self._specific_massa = float_convert(massa)
        if self._specific_massa == -1:
            self._specific_massa = 25

    def asphalt_massa_calc(self):
        return self._length * self._heigth * self._width * self._specific_massa


road = Road(length=5000, width=20)
road.set_heigth(6)
print(f'Масса асфальта: {road.asphalt_massa_calc() / 1000}(тон.)')
