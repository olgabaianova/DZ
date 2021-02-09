#l=[2,2,6,8,11,8,55,98,11,6]
def func(lst):
    for el in lst:
        if lst.count(el)==l:
            yield el
    test_list [2,2,6,8,11,8,55,98,11,6]
print ([el for el in func(test_list)])
