l=[1, 5, 8, 8,6, 4]

while True:
    new_digit = input ('Введите число: ')
    if new_digit=='q':
        break
        new_digit = int(new_digit)
        for i in range (1, len(l)):
            if new_digit>=max(l):
                l.insert(0,new_digit)
                break
            elif new_digit <= min(l):
                l.append(new_digit)
                break
            elif l[i-1]>= new_digit >=l[i]:
                l.insert(i,new_digit)
                break
    print(l)

#вводила переменную new_el вместо new_digit выдавал кучу ошибок
# поменяла название переменной - ошибки не выдает, но новую переменную в список не ставит
# new_digit = int(new_digit) ругается на эту строку, что-то в ней неверно((( задача сложная для меня