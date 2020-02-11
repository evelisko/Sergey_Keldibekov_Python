# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с
# индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения
# списка элементов необходимо использовать функцию input().

# items_count = int(input('Задайте количество элементов в списке: '))
# items = []
items_count = 7
i = 7
items = [1, 2, 3, 4, 5, 6, 7]
while i < items_count:
    try:
        items.append(int(input(f'{i + 1}) ')))
    except ValueError as e:
        print(f'случилась ошибка ValueError: {e}')
    else:
        i += 1

print(f'Исходный массив: {items}')
i = 1
while i < items_count:
    items[i - 1], items[i] = items[i], items[i - 1]
    i += 2

print(f'Преобразованный: {items}')

# time_in_seconds = '100360'
# print('Введено число: ' + time_in_seconds)
# while not time_in_seconds.isdigit():
#     time_in_seconds = input('Введите время в секундах: ')
#
# time_in_seconds = int(time_in_seconds)
#
# time_in_seconds /= 3600
# hours = int(time_in_seconds)
# time_in_seconds = (time_in_seconds - hours) * 60
# minutes = int(time_in_seconds)
# seconds = int((time_in_seconds - minutes) * 60)
#
# print("%02d:%02d:%02d" % (hours, minutes, seconds))
