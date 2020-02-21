# 3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


with open('task_3_file.txt', 'r', encoding='utf-8') as f_obj:
    content_as_list = f_obj.read().splitlines()

print(content_as_list)
lines_count = len(content_as_list)
print(lines_count)

pur_emplore = []
middle_selary = 0
for el in content_as_list:
    name, selary = el.split()
    selary = float(selary)
    middle_selary += selary / lines_count
    if selary < 20000.0:
        pur_emplore.append(name)


print(middle_selary)
print(pur_emplore)
