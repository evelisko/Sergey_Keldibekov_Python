# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

# input_string = input('Ведите строку: ').split()
simple_str = 'Числа шестнадцетиричной системы счисления -  0123456789ABCDEF'
input_string = simple_str.split()
print(input_string)
# i = 1
# for el in input_string:
#     print(f'{i}) {el[:10]}')
#     i += 1

for ind, el in enumerate(input_string, 1):
    print(f'{ind}) {el[:10]}')
