# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

while True:
    value = '9'
    # value = input('Введите целое число в диапазоне 0..9: ')
    if value.isdecimal():
        value = int(value)
        if (value >= 0) and (value < 10):
            break
    continue

print(f'Введено число: {value}')

value10 = value * 10 + value
value100 = value10 * 10 + value
result_value = value + value10 + value100

print(f'{value} + {value10} + {value100} = {result_value}')

# [::-1] - строrf в обратном порядке выводится
# b =copy.copy(a)
# b = copy.deepcopy(a)
# d = a[:]
# print(dir(a))# выводт список операция доя этого класса.
