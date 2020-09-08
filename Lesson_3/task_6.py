# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def title_acsii(string_data):
    string_data = str(string_data)
    tmp = ord(string_data[0]) - 32
    # string_data = chr(tmp) + string_data[1:]    # так более наглядно, по моему
    string_data = f'{chr(tmp)}{string_data[1:]}'  # а так менне
    return string_data


text_string = input('Введите строку из прописных букв: ')
for str_element in text_string.split():
    print(f'{title_acsii(str_element)} ', end='')
print()

print('С использованем лямба-функции')
word_list = list(map(lambda x: title_acsii(x), text_string.split()))
for str_element in word_list:
    print(f'{str_element} ', end='')
