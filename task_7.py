# 7) Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка,
# издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее ​ не включать​ .
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{​ "firm_1"​ : ​ 5000​ , ​ "firm_2"​ : ​ 3000​ , ​ "firm_3"​ : ​ 1000​ }, {​ "average_profit"​ : ​ 2000​ }]
# Подсказка: использовать менеджер контекста.


import json


def profit_calc(val_str):
    values = val_str.split()
    return values[0].rstrip(), int(values[2]) - int(values[3])


with open('task_7_file.txt', 'r', encoding='utf-8') as f_obj:
    profit_list = f_obj.read().splitlines()
    print(profit_list)

firms_dict = dict(map(profit_calc, profit_list))
in_profit_firms = 0
average_profit = 0.0

for firm_info in firms_dict.values():
    if firm_info > 0:
        in_profit_firms += 1
        average_profit += firm_info

average_profit /= in_profit_firms
print(firms_dict)
print(f'Среднее значение прибыли: {average_profit}')

with open('firms_data.json', 'w', encoding='utf-8') as f_obj:
    json.dump([firms_dict, {'average_profit': average_profit}], f_obj)

