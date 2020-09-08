# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя,
# фамилия,
# год рождения,
# город проживания,
# email,
# телефон.
# Функция должна принимать параметры как именованные аргументы !!!
# Реализовать вывод данных о пользователе одной строкой.

user_atribute = ['Имя', 'Фамилия', 'Год рождения', 'Место проживания', 'Почта', 'Телефон']


def print_user_date(first_name, last_mane, birdth_year, city, email='', phone_number=''):  # Копипаст сделал из-за того,
    print(f'{user_atribute[0]}: {first_name}, ', end='')                                   # что именнованные аргументы передавать нужно.
    print(f'{user_atribute[1]}: {last_mane}, ', end='')                                    # Здесь опитмальнее в массив все запихнуть было.
    print(f'{user_atribute[2]}: {birdth_year}, ', end='')
    print(f'{user_atribute[3]}: {city}, ', end='')
    print(f'{user_atribute[4]}: {email}, ', end='')
    print(f'{user_atribute[5]}: {phone_number} ')


user_data = {
    'first_name': 'Иван',
    'last_mane': 'Иванов',
    'birdth_year': 1995,
    'city': 'Москва',
    'email': 'exemple@mail.ru',
    'phone_number': '8(907)754-83-12',
}

print_user_date(first_name=user_data['first_name'], last_mane=user_data['last_mane'],
                birdth_year=user_data['birdth_year'], city=user_data['city'],
                email=user_data['email'], phone_number=user_data['phone_number'])


# Вариант №2 --------------------------------------------------------------------------------------------------

def print_user_dat_xe(**kwargs):
    i = 0
    for atrib in kwargs.values():
        print(f'{user_atribute[i]}: {atrib}  ', end='')
        i += 1
    print()


print_user_dat_xe(**user_data)
