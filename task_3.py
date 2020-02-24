# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и
# ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


from user_functions import float_convert


class Worker(object):

    def __init__(self, name, surname, position):
        self._name = name
        self._surname = surname
        self._position = position
        self._income = {"wage": None,
                        "bonus": None}  # по идее, этот атрибут можно здесь не определять а задать в дочернем классе.

    def __str__(self):
        return f'{self._name} {self._surname}'

    def set_income(self, **income):
        if float_convert(income['wage']) != -1 and float_convert(income['bonus']) != -1:
            self._income = income
            if self._income['wage'] < 12000:
                print(f'зарплата работника ({self._name} {self._surname}) не может быть ниже прожиточного минимума!!!')
                # self._income['wage'] = 12000   # установить зарплату равную прожиточнуму минимуму
        else:
            print('не верный формат для данных')


class Position(Worker):

    def __init__(self, name, surname, position, wage=12000, bonus=0):
        super().__init__(name, surname, position)
        self.set_income(wage=wage,bonus=bonus)

    def get_full_name(self):
        return f'{self._name} {self._surname} - {self._position}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker_1 = Position('Иван', 'Иванов', position='Водитель', wage=12000, bonus=1500)
print(worker_1.get_full_name())
print(f'Зарплата: {worker_1.get_total_income()}')

worker_2 = Position('Юрий', 'Иванов', position='Водитель')
worker_2.set_income(wage=10000, bonus=1600)
print(worker_2.get_full_name())
print(f'Зарплата: {worker_2.get_total_income()}')
