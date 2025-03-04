t = int(input())

def DH(x): return abs(S - (xm := x * m) * (xm + 1))
def DV(x): return abs(S - x * n * (x + nm - m + 1))

for _ in range(t):
    n,m = map(int, input().split())
    nm = n * m
    P = nm * (nm + 1)
    S = P / 2
    
    H = int(0.5 * ((1+2*P)**0.5 - 1) / m)
    dH = DH(H)
    if (tmp := DH(H + 1)) < dH:
        H += 1
        dH = tmp
    
    V = int(0.5 * (( (nm+1)**2 + m*m )**0.5 - nm + m -1))
    dV = DV(V)
    if (tmp := DV(V + 1)) < dV:
        V += 1
        dV = tmp
    
    if dH < dV:
        print(f"H {H + 1}")
    else:
        print(f"V {V + 1}")