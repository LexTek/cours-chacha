from functools import reduce
from random import randint

for gpt in range(0, 10):
    print(gpt)

lst = [2*i for i in range(0, 4)]
lst2 = [0, 2, 4, 6]
lst = lst + lst2

print(lst)
for i in range(0, len(lst)):
    lst[i] = 0
print(lst)

lst = lst + [3]

print(lst)

somme = 0
for el in lst:
    somme = somme + el

print(somme)

somme = reduce(lambda x, y : x + y, lst)

print(somme)

lst = [i for i in range(0, 10)]

lst = list(map(lambda x : x + 1, filter(lambda x: x % 2 == 0, lst)))

print(lst)

lst = [randint(0, 100) for i in range(0, 10)]

lst2 = sorted(lst)

print(lst)
print(lst2)