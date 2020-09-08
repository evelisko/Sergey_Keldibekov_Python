# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class Complex:
    def __init__(self, a, ja):
        self._a = a
        self._ja = ja

    def __str__(self):
        if self._ja > 0:
            return f'({self._a} + {self._ja}j)'
        else:
            return f'({self._a} - {abs(self._ja)}j)'

    @property
    def imag(self):
        return self._a

    @property
    def real(self):
        return self._ja

    def __add__(self, other):  # +
        a = self._a + other.imag
        ja = self._ja + other.real
        return Complex(a, ja)

    def __sub__(self, other):  # -
        a = self._a - other.imag
        ja = self._ja - other.real
        return Complex(a, ja)

    def __mul__(self, other):  # *
        a = self._a * other.imag - self._ja * other.real
        ja = self._a * other.real + self._ja * other.imag
        return Complex(a, ja)

    def __truediv__(self, other):  # /
        a = (self._a * other.imag + self._ja * other.real) / (other.imag ** 2 + other.real ** 2)
        ja = (other.imag * self.real - self._a * other.real) / (other.imag ** 2 + other.real ** 2)
        return Complex(a, ja)


num_1 = Complex(1, -5)
num_2 = Complex(5, 2)

print(num_1)
print(num_2)

num_3 = num_1 + num_2
num_4 = num_3 + num_1 + num_2

print(num_4, end='\n\n')

print('Cложение\n----------------------------')
result_num = num_1 + num_2
print(f'1){num_1} + {num_2} = {result_num}')

print('\nВычитаие\n----------------------------')
result_cell = num_1 - num_2
print(f'2){num_1} - {num_2} = {result_num}')

print('\nУмножение\n----------------------------')
result_num = num_1 * num_2
print(f'4){num_1} * {num_2} = {result_num}')

print('\nДеление\n----------------------------')
num_1 = Complex(2, 0)
num_2 = Complex(1, 2)
result_num = num_1 / num_2
print(f'4){num_1} / {num_2} = {result_num}')
