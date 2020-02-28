# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self):
        self._size = None
        self._used_fabrics = None

    @abstractmethod
    def calc_used_fabrics(self):
        pass

    @property
    def used_fabrics(self):
        return self._used_fabrics

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        try:
            float(value)
        except Exception as ex:
            print('значение должно соответствовать типу float')
        else:
            self._size = float(value)
            self.calc_used_fabrics()

    def __str__(self):
        return f'Размер:{self._size}, иcпользовано ткани: {self._used_fabrics:.3f}'


class Coat(Clothing):  # Пальто
    def __init__(self, size):
        super().__init__()
        self._size = size
        self.calc_used_fabrics()

    def calc_used_fabrics(self):
        self._used_fabrics = self._size / 6.5 + 0.5


class Costume(Clothing):  # Костюм

    def __init__(self, heigth):
        super().__init__()
        self._size = heigth
        self.calc_used_fabrics()

    def calc_used_fabrics(self):
        self._used_fabrics = 2 * self._size + 0.3


costume_1 = Costume(60)
coat_1 = Coat(43)

print(costume_1)
print(coat_1)
print('-------------------------------------')

costume_used_fabrics = costume_1.used_fabrics
coast_used_fabrics = coat_1.used_fabrics

print(f'Расход ткани на костюм: {costume_used_fabrics:.3f}')
print(f'Расход ткани на пальто: {coast_used_fabrics:.3f}')

summary_used = coat_1.used_fabrics + costume_1.used_fabrics

print(f'Общий расход ткани: {summary_used:.3f}')
