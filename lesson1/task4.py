n = int (input('Введите целое положительное число: '))
max_digit = 0
while n>0:
    if n % 10==9:
        max_digit = 9
         break
    if n % 10 > max_digit:
        max_digit =  n % 10
    n//=10
print (f'Максимальная цифра - {max_digit}')





