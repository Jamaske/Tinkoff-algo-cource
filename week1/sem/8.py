from random import randint
from time import time_ns
from math import log2
n = 10 ** 6
m = n

a = sorted([randint(1,32 * n) for _ in range(n)])
b = sorted([randint(1,32 * n) for _ in range(m)])

t1 = time_ns()

i = len(a)
c1 = 0
for j, b_val in enumerate(b):
     # можно вместо линейного применить експоненциальный (2 бин поиска: 1 - поиск верхней границыб 2 - уточнение значения)
    while i and a[-i] <= b_val:
        i -= 1
    c1 += i


t2 = time_ns()

A = {} #a iters between each b iter
B = {} #b iters between each a iter
i = len(a)
c2 = 0
cnt2 = 0
for b_val in b:
    cnt1 = 0
    while i and a[-i] <= b_val:
        B[cnt2] = B.get(cnt2, 0) + 1
        cnt2 = 0
        cnt1 += 1
        i -= 1
    A[cnt1] = A.get(cnt1, 0) + 1
    if not cnt1: cnt2 += 1

    c2 += i


t3 = time_ns()

A_s = sum(A.values())
B_s = sum(B.values())
A_d = []
B_d = []
for key in range(max(*A.keys(), *B.keys())):
    A_d.append(A.get(key, 0) / A_s)
    B_d.append(B.get(key, 0) / B_s)
    print(f"{key}: {A_d[-1]}  {B_d[-1]}")


A_score = sum((i+1) * p for i, p in enumerate(A_d))
B_score = sum((i+1) * p for i, p in enumerate(B_d))
print(A_score, B_score)

A_score = sum((log2(i + 2) * p for i, p in enumerate(A_d)))
B_score = sum((log2(i + 2) * p for i, p in enumerate(B_d)))
print(A_score, B_score)


print(f"var 1 res {c1} time {(t2 - t1) / 10 ** 9} ns")
print(f"var 2 res {c2} time {(t3 - t2) / 10 ** 9} ns")
