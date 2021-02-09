def fact(n):
    num=1
    for i in range (1, n+1):
        num*=i
        yield num
    for el in fact(3):
        print(el)
    3
