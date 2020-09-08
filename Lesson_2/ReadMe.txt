Feedback
----------------------------------------------------------------
	
	во 2 дз с нечетным и четным размером списка надо аккуратно
month_list[month_index - 1] - верная идея
5 дз для value = 8 не работает
в 6м дз "items = list((zip(goods[0][1].values(), goods[1][1].values(), goods[2][1].values())))" - а если будет 150 наименований?
----------------------------------------------------------------
Да, верно 6 -м задании перемудрил немного. Мне просто интерессно было разобраться с работой операторов. И через них задачу решить.
В 5-м задании признаю. недосмотрел. Вот так будет работать:
value = 8
ind = len(my_list)
while ind > 0:
if value <= my_list[ind - 1]:
my_list.insert(ind, value)
print(f'В позицию - {ind}')
break
ind -= 1

if ind == 0:
my_list.insert(ind, value)

https://github.com/evelisko/Sergey_Keldibekov_Python/pull/3