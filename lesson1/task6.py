a = float(input('Введите расстояние в км, которое пробежал спортмен в первый день'))
b = float(input('Введите расстояние в  км, которое необходимо достичь  спортмену'))
counter = 1
while a<= b:
    print(f'{counter} день: {round(a,2)} км.')
    a = a*1.1
    counter +=1
print (f'{counter} день: {round(a,2)} км.')
print (f'Спортсмен пробежит не менее {b} км на {counter} день')

# для меня это сложная задача