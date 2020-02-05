# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

while True:
    value = '235859'
    # value = input('Введите целое положительное число: ')
    if value.isdecimal():
        break
    continue

print(f'Введено число: {value}')

max_value = 0
for digit in value:
    if int(digit) > max_value:
        max_value = int(digit)

print(f'Самая большая цифра в числе - это {max_value}')
