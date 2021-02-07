def info (name, surname, year_of_birday, city, email, phone):
    return f' имя:{name}, фамилия:{surname}, год рождения:{year_of_birday}, город:{city}, электронная почта:{email}, телефон:{phone}'
print(info(
    name=input('Введите имя: '),
    surname=input('Введите фамилию:'),
    year_of_birday=input('Введите год рождения: '),
    city=input('Введите город: '),
    email=input('Введите электронную почту: '),
    phone=input('Введите номер телефона: ')
))