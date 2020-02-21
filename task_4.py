# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.


digits_list = ['Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять']


def tranlete_word(val_str):
    words = val_str.split()
    words[0] = digits_list[int(words[2]) - 1]
    return f'{words[0]} {words[1]} {words[2]}\n'


with open('task_4_file.txt', 'r', encoding='utf-8') as f_obj:
    lines_list = f_obj.read().splitlines()

print(lines_list)

new_lines_list = list(map(tranlete_word, lines_list))

with open('task_4_file_1.txt', 'w', encoding='utf-8') as f_obj:
    f_obj.writelines(new_lines_list)
