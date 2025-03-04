a, b, c, d = map(int, input().split())


s = abs(b) + abs(c) + abs(d)
if a > 0:
    h = max(1, s / a)
    l = -h
else:
    h = min(-1, s / a)
    l = -h

while abs(h - l) > 0.5e-6:
    
    m = (h + l) / 2
    #print(l,h)
    if ((((a)*m) + b)*m + c)*m + d > 0:
        h = m
    else:
        l = m
print((h + l) / 2)

