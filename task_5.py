# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

# while True:
profit = input('Введите величину прибыли фирмы: ')
costs = input('Введите величину издержек: ')
#  val1 = profit.isdigit()
#    val2 = costs.isdigit()
#    if costs.isdigit():       # and profit.isdigit():
#        break
#    continue


profit = float(profit)
costs = float(costs)
is_profit = 0

if profit > costs:
    print('Фирма приносит прибыль')
    print('Рентабельность: %.3f' % (profit / costs))
    is_profit = True
elif profit < costs:
    print('Фирма работает в убыток')
else:
    print('Фирма работает в ноль')

if is_profit:
    while True:
        worker_count = input('Введите количество сотрудников: ')
        if worker_count.isdecimal():
            break
        print('не верный формат ввода. Попробуйте еще')
        continue
    worker_count = int(worker_count)
    print('В рассчете на одного сотрудника прибыл составляет %.3f' % (profit/worker_count))
