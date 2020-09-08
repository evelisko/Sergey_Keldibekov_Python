# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.


class Stationery(object):
    def __init__(self):
        self._title = ''

    def draw(self):
        print(f'{self._title} Запуск отрисовки')


class Pencil(Stationery):
    def __init__(self):
        super().__init__()
        self._title = 'Pencil'

    def draw(self):
        print(f'{self._title} Делаем набросок')


class Handle(Stationery):
    def __init__(self):
        super().__init__()
        self._title = 'Handle'

    def draw(self):
        print(f'{self._title} Выделяем текст')


class Pen(Stationery):
    def __init__(self):
        super().__init__()
        self._title = 'Pen'

    def draw(self):
        print(f'{self._title} Пишем письмо')


stationery_1 = Pen()
stationery_2 = Pencil()
stationery_3 = Handle()

stationery_1.draw()
stationery_2.draw()
stationery_3.draw()
