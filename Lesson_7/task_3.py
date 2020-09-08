# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()),
# умножение (mul()), деление (truediv()).Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение. Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр
# класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида **\n\n***..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
# вернет строку: **\n\n. Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: **\n\n***.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.


class Cell:
    def __init__(self, cell_count):
        self._cell_count = None
        self.cell_count = cell_count

    def __str__(self):
        return f'{self._cell_count}'

    @property
    def cell_count(self):
        return self._cell_count

    @cell_count.setter
    def cell_count(self, count):
        try:
            int(count)
        except Exception as ex:
            print(f'Количество ячеек в клетке должно иметь целочисленное значение {ex}')
        else:
            self._cell_count = int(count)

    def __add__(self, other):  # +
        return Cell(self._cell_count + other.cell_count)

    def __sub__(self, other):  # -
        result = self._cell_count - other.cell_count
        if result > 0:
            return Cell(result)
        else:
            print('результат не может быть меньше 1')

    def __mul__(self, other):  # *
        return Cell(self._cell_count * other.cell_count)

    def __truediv__(self, other):  # /
        result = self._cell_count // other.cell_count
        return Cell(result) if result > 0 else print('результат не может быть меньше 1')

    def make_order(self, line_count):
        cells = ''
        cell_line = 1
        for __ in range(self._cell_count):
            if cell_line > line_count:
                cells += '\n'
                cell_line = 1
            cells += '*'
            cell_line += 1
        return cells


cell_1 = Cell(10)
cell_2 = Cell(5)

print('Cложение\n----------------------------')
result_cell = cell_1 + cell_2
print(f'1){cell_1.cell_count} + {cell_2.cell_count} = {result_cell}')

print('\nВычитаие\n----------------------------')
result_cell = cell_2 - cell_1
print(f'2){cell_2.cell_count} - {cell_1.cell_count} = {result_cell}')

result_cell = cell_1 - cell_2
print(f'3){cell_1.cell_count} - {cell_2.cell_count} = {result_cell}')

print('\nУмножение\n----------------------------')
result_cell = cell_1 * cell_2
print(f'4){cell_1.cell_count} * {cell_2.cell_count} = {result_cell}')

print('\nДеление\n----------------------------')

result_cell = cell_2 / cell_1
print(f'5){cell_2.cell_count} / {cell_1.cell_count} = {result_cell}')

result_cell = cell_1 / cell_2
print(f'6){cell_1.cell_count} / {cell_2.cell_count} = {result_cell}\n----------------------------')
