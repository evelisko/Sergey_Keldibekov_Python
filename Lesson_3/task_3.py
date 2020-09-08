# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


# digit_1 = int(input('Введите 1-е чило: '))
# digit_2 = int(input('Введите 2-е чило: '))
# digit_3 = int(input('Введите 3-е чило: '))

digit_1 = 12
digit_2 = 1
digit_3 = 7


# 1-й вариант.-------------------------------------------
def my_func(one, two, three):
    digits = sorted([one, two, three])
    return digits[2] + digits[1]


print(my_func(digit_1, digit_2, digit_3))


# 2-й вариант.-------------------------------------------
def my_func_ex(one, two, three):
    digits = [one, two, three]
    i = 0
    while i < len(digits) - 1:
        if digits[i] < digits[i + 1]:
            digits[i], digits[i + 1] = digits[i + 1], digits[i]
        i += 1
    return digits[0] + digits[1]


print(my_func_ex(digit_1, digit_2, digit_3))
