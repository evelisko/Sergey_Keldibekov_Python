# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
#
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.


class DigitsError(ValueError):
    pass


def float_convert(val):
    try:
        val = float(val)
    except:
        val = -1
    return val


print('Введение символа "q" останавливает выполнение программы')
values_list = []
while True:
    digit_value = input('Введите число: ')
    digit_value = digit_value.replace(' ', '')
    if digit_value == 'q':
        break
    try:
        if float_convert(digit_value) == -1:
            raise DigitsError(f'digits value error: {digit_value}')
    except DigitsError as e:
        print(e)
    else:
        if digit_value.isdigit():
            values_list.append(int(digit_value))
        else:
            values_list.append(float(digit_value))

print(values_list)
print('Выполнение программы завершено ! ')

#
# class Cell:
#     def __init__(self, cell_count):
#         self._cell_count = None
#         self.cell_count = cell_count
#
#     def __str__(self):
#         return f'{self._cell_count}'
#
#     @property
#     def cell_count(self):
#         return self._cell_count
#
#     @cell_count.setter
#     def cell_count(self, count):
#         try:
#             int(count)
#         except Exception as ex:
#             print(f'Количество ячеек в клетке должно иметь целочисленное значение {ex}')
#         else:
#             self._cell_count = int(count)
#
#     def __add__(self, other):  # +
#         return Cell(self._cell_count + other.cell_count)
#
#     def __sub__(self, other):  # -
#         result = self._cell_count - other.cell_count
#         if result > 0:
#             return Cell(result)
#         else:
#             print('результат не может быть меньше 1')
#
#     def __mul__(self, other):  # *
#         return Cell(self._cell_count * other.cell_count)
#
#     def __truediv__(self, other):  # /
#         result = self._cell_count // other.cell_count
#         return Cell(result) if result > 0 else print('результат не может быть меньше 1')
#
#     def make_order(self, line_count):
#         cells = ''
#         cell_line = 1
#         for __ in range(self._cell_count):
#             if cell_line > line_count:
#                 cells += '\n'
#                 cell_line = 1
#             cells += '*'
#             cell_line += 1
#         return cells
#
#
# cell_1 = Cell(10)
# cell_2 = Cell(5)
#
# print('Cложение\n----------------------------')
# result_cell = cell_1 + cell_2
# print(f'1){cell_1.cell_count} + {cell_2.cell_count} = {result_cell}')
#
# print('\nВычитаие\n----------------------------')
# result_cell = cell_2 - cell_1
# print(f'2){cell_2.cell_count} - {cell_1.cell_count} = {result_cell}')
#
# result_cell = cell_1 - cell_2
# print(f'3){cell_1.cell_count} - {cell_2.cell_count} = {result_cell}')
#
# print('\nУмножение\n----------------------------')
# result_cell = cell_1 * cell_2
# print(f'4){cell_1.cell_count} * {cell_2.cell_count} = {result_cell}')
#
# print('\nДеление\n----------------------------')
#
# result_cell = cell_2 / cell_1
# print(f'5){cell_2.cell_count} / {cell_1.cell_count} = {result_cell}')
#
# result_cell = cell_1 / cell_2
# print(f'6){cell_1.cell_count} / {cell_2.cell_count} = {result_cell}\n----------------------------')
