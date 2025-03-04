n = int(input())

a = list(range(n))

j = n - 1
for i in range(n):
    p = (i + j) // 2
    a[i], a[p] = a[p], a[i]

#print(a)

b = [None] * n
for i, idx in enumerate(a):
    b[idx] = i + 1

print(' '.join(map(str, b)))