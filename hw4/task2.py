# [6, 9, 5, 22, 15, 67,35]
def func(l):
    for i in range (1,len(l)):
        if l[i]>l[i-1]:
            yield l[i]
    test_list=[6,9,5,22,15,67,35]
    new_list=[el for el in func(test_list)]
    print (new_list)
    6
    9
5
22
