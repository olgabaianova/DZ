a =int(input( 'Введите число a: '))
b = int(input('Введите число b:'))
def fun (a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print ('Ошибка: вы делите на ноль: ')
    return
print(fun(a,b))
