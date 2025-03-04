
def qsort(a, left, right):
    global swp, cmp
    if right <= left:
        return
    i, j = left, right
    q = a[(i+j)//2]
    while i <= j:
        cmp += 2
        while a[i] < q:
            i += 1
            cmp += 1
        while q < a[j]:
            j -= 1
            cmp += 1
        if i <= j:
            swp += 1
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    qsort(a, left, j)
    qsort(a, i, right)


def qsort2(a, left, right):
    global swp, cmp
    if right <= left:
        return
    i, j = left, right
    p = a[(i+j)//2]
    while i < j:
        cmp += 2
        while a[i] < p:
            i += 1
            cmp += 1
        while p < a[j]:
            j -= 1
            cmp += 1
        if i < j:
            swp += 1
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        else:
            break
    else:
        if i == j:
            cmp += 1
            if a[i] <= p: i += 1
            if a[i] >= p: j -= 1
    
    qsort2(a, left, j)
    qsort2(a, i, right)

a = [9, 3, 7, 5, 1, 2, 4, 6, 8, 10]
swp = 0
cmp = 0
b = a.copy()

qsort(a, 0, len(a)-1)
print(a)
print(f"{cmp = } {swp = }")

# swp = 0
# cmp = 0
# qsort2(b, 0, len(b) - 1)
# print(b)
# print(f"{cmp = } {swp = }")
