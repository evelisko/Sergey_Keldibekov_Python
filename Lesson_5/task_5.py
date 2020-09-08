# 5) Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.

import random
from functools import reduce

with open('task_5_file.txt', 'w', encoding='utf-8') as f_obj:
    digits_list = [str(random.randint(0, 30)) for __ in range(7)]
    print(digits_list)
    for line in digits_list:
        f_obj.write(f'{line} ')


with open('task_5_file.txt', 'r+', encoding='utf-8') as f_obj:
    lines_list = list(map(int, f_obj.readline().split()))
    # values_sum = reduce(lambda x, y: x + y, lines_list)
    values_sum = sum(lines_list)
    print(values_sum)
    f_obj.write(f'\nСумма чисел первой сроки: {values_sum}')
