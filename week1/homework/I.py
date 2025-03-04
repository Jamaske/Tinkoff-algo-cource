n = int(input())

right= [False] * (n+1)
array = [False] * n


order = map(int, input().split())
left_zero = n - 1

ans = [1]

for i, idx in enumerate(order):
    idx -= 1
    array[idx] = True
    if idx == left_zero:
        left_zero -= 1
        while left_zero >= 0 and array[left_zero]: left_zero -= 1
    ans.append(left_zero + i + (3 - n))
print(' '.join(map(str, ans)))
