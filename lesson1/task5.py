a = float (input('Введите значение выручки:'))
b = float (input('Введите значение издержек:'))
if a > b:
    profit = a - b
    print (f'фирма работает с прибылью, рентабельность составляет {profit /a:2f}')
    count_workers = int(input('Введите количество сотрудников фирмы: '))
    print (f'Прибыль фирмы на одного сотрудника: {profit / count_workers}')
elif a < b:
    print ('фирма работает в убыток')
else:
    print('доходы и расходы равны')


# влад, почему использовали функцию?