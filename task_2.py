# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


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
