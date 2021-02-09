from sys import argv
def salary (hours, koef, bonus):
    return f'заработная плата составляет: {hours}*{koef}+{bonus} = {float(hours)+float(koef)+float(bonus)}'
_, hours, koef, bonus=argv
print(salary(hours,koef,bonus))


# не поняла, как запустить через консоль с параметрами