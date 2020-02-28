# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix():

    def my_func(self, a, b):
        return a + b

    def __init__(self, argv):
        self.matrix = argv

    def __str__(self):
        strs = ''
        for el in self.matrix:
            strs += '|\t' + '\t|\t'.join(map(str, el)) + '\t|\n'
        return strs

    def __add__(self, other):
        result = []
        try:
            for ex, ey in map(lambda *x: x, self.matrix, other.matrix):
                result.append(list(map(lambda x, y: x + y, ex, ey)))
        except Exception as ex:
            print(f'Складываемые матрицы имеют разную размерность {ex}')
        else:
            return Matrix(result)


simple_matrix = [[1, 2, 3], [4, 6, 7], [8, 9, 10]]
simple_matrix_1 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
matrix_1 = Matrix(simple_matrix)
matrix_2 = Matrix(simple_matrix_1)
print('Матрица A:\n-------------------------------')
print(matrix_1)
print('Матрица B:\n-------------------------------')
print(matrix_2)

matrix_3 = matrix_1 + matrix_2

print('Результат сложения \n-------------------------------')
print(matrix_3)
