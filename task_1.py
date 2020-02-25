# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix(object):

    def __init__(self,*args):
        self._matrix = args

    def __str__(self):
       strs = ''
       for el in self._matrix:  #todo сделатьправильный вывод.
            strs += ' '.join(map(string, el)) + '\n'
       return strs

    # сложение матриц.

simple_matrix = [[1,2,3],[4,6,7],[7,8,9]]
matrix_1 = Matrix(simple_matrix)
print(matrix_1)





















# import time
#
#
# class TrafficLight(object):
#     _colors = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}
#
#     def __init__(self):
#         self._color = self._colors['Красный']
#
#     def running(self):
#         for cl, tm in self._colors.items():
#             self._color = cl
#             print(self._color)
#             # print(f'{self._color} {tm}сек.')
#             time.sleep(tm)
#
#     def get_sate(self):
#         return self._color
#
#
# trafic_lighter = TrafficLight()
# trafic_lighter.running()
# print('Программа завершила работу')
