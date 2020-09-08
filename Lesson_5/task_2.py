# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.


with open('task_2_file.txt', 'r', encoding='utf-8') as f_obj:
    content_as_list = f_obj.read().splitlines()

print(content_as_list)

lines_count = len(content_as_list)
print(f'Всего строк: {lines_count}')

c = 1
for el in content_as_list:
    word_count = el.split()
    print(f'{c}:  {len(word_count)}')
    c += 1

