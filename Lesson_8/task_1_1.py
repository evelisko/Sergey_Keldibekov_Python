# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date(object):

    def __init__(self, *args):
        self._date = {'day': args[0], 'month': args[1], 'year': args[2]}

    @staticmethod
    def data_validate(*args):
        is_date = True if args[0] in range(1, 32) \
            else print(f'{args[0]} значение дня в месяце должно быть в диапазоне 1-31')
        is_month = True if args[1] in range(1, 13) \
            else print(f'{args[1]} значение месяца должно быть в диапазоне 1-12')
        return is_date and is_month

    @classmethod
    def data_converter(cls, val=''):
        val = val.replace(' ', '')
        data_list = val.split('-')
        values = []
        for el in data_list:
            if el.isdecimal():
                values.append(int(el))
            else:
                print(f'значение {el} не является числом')
        if cls.data_validate(*values):
            return cls(*values)

    def __str__(self):
        return f'{self._date["day"]:02d}.{self._date["month"]:02d}.{self._date["year"]:02d}'


date_1 = Date(1, 11, 2015)
date_2 = Date.data_converter('02 - 05 - 2020')
print(date_1)
print(date_2)
