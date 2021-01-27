time = int (input ('Введите время в секундах: '))
minutes = time // 60
seconds = time % 60
hours = minutes // 60
minutes = seconds % 60
print (f'{hours:02}:{minutes:02}:{seconds:02}')
