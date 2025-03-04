from random import randint

n = 10
a = [randint(1,20) for i in range(n)]
b = [None] * n
c = 0
for i, el in enumerate(a):
    c += el
    b[i] = c


def search_dc(arr:list, value:int, logger = None) -> int:
    l = 0
    r = len(arr) - 1
    while l < r:
        m = (l + r + 1) // 2

        #logger((l,r,m))

        if arr[m] <= value:
            l = m
        else:
            r = m - 1
    return l

X = 40

num = search_dc(b, X) + 1
print(a)
print(b)
print(num)
