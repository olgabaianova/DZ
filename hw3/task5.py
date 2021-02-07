l = [6, 9, 3, 4, 1]
new_el = int(input('Введите число: '))
if new_el =='q':
    break
for i in range(1, len(l)):
    if new_el >= max(l):
        l.insert(0, new_el)
        break
    elif new_el <= min(l):
        l.append(new_el)
        break
    elif l[i - 1] >= new_el >= l[i]:
        l.insert(i, new_el)
        break
print(l)

# что-то не так не получилось