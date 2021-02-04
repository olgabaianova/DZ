worlds = input('Ведите слова через пробел: ').split()
for i , world in enumerate (worlds, 1):
    print (f' {i}:{world[0:10]}')
