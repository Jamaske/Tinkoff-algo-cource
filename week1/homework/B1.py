input()
a = list(map(int, input().split()))
b = map(int, input().split())

def search(arr: list, value: int) -> int:
    l = 0
    r = len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] < value:
            l = m + 1
        else:
            r = m
    return l

for req in b:
    i = search(a, req)
    r = a[i]
    if i == 0:
        print(r)
        continue
    l = a[i-1]
    if r - req < req - l:
        print(r)
    else:
        print(l)
