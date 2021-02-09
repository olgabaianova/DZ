import operator
from functools import reduce
print (reduce (operator.mul,[el for el in range(100,1001) if el %2==0 ]))
#вывел неверно, бесконечную строку чисел((((