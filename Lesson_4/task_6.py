# 6) Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию ​count() и cycle() модуля itertools.​ Обратите внимание, что
# создаваемый  цикл  не  должен  быть  бесконечным.  Необходимо  предусмотреть  условие  его
# завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
# завершаем  цикл.  Во  втором  также  необходимо  предусмотреть  условие,  при  котором
# повторение элементов списка будет прекращено.


from itertools import count
from itertools import cycle
from itertools import islice

print('Итератор itertools.count()')
for el in islice(count(7), 6):
    print(el, end=' ')
print(end='\n\n')

print('Итератор itertools.cycle()')

data_list = ['A', 'C', '-', 'D', 'C']

for el in islice(cycle(data_list), 7):
    print(el, end=' ')
print()