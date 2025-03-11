N = int(input())
data = [None] * (N + 2)
data[0] = 2_000_000_000
data[N + 1] = -2_000_000_000

for idx, num in enumerate(map(int, input().split()), start = 1):
    par = idx // 2
    while num > data[par]:
        data[idx] = data[par]
        idx = par
        par = par // 2
    data[idx] = num


res = [None] * N
for size in range(N, 0,-1):
    res[size - 1] = data[1]
    val = data[size]
    data[size] = -2_000_000_000

    idx = 1
    while (ch := 2 * idx) <= size:
        if data[ch] < data[ch+1]: ch += 1
        if data[ch] > val:
            data[idx] = data[ch]
            idx = ch
        else:
            break
    
    data[idx] = val

print(' '.join(map(str, res)))


