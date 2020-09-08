# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.


def devision_of_numbers(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print(f'Функция devision_of_numbers выдала исключение  - деление на ноль \n '
              f'второе значение не может равняться нулю')


# value1 = int(input('Введите значение делимого числа: '))
# value2 = int(input('Введите значение делителя: '))

value1 = 5
value2 = 0

print(f'Результат операции: {devision_of_numbers(value1, value2)}')
