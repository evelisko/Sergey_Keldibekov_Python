# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_seconds = '100360'
print('Введено число: ' + time_in_seconds)
while not time_in_seconds.isdigit():
    time_in_seconds = input('Введите время в секундах: ')

time_in_seconds = int(time_in_seconds)

time_in_seconds /= 3600
hours = int(time_in_seconds)
time_in_seconds = (time_in_seconds - hours) * 60
minutes = int(time_in_seconds)
seconds = int((time_in_seconds - minutes) * 60)

print("%02d:%02d:%02d" % (hours, minutes, seconds))
