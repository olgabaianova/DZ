from itertools import count, cycle
print('')
start = int(input("введите число, с которого нужно начать генерацию"))
end = int(input("введите число, на котором следует остановиться"))
counter = count(start)
for i in range(start, end+1):
    print (next(counter))

