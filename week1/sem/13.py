from random import randint
n = 10
A = [randint(1,5) for i in range(10)]
B = [randint(1,50) for i in range(10)]
D = [randint(1,5) for i in range(10)]
monay = 10



#normalize for cost
for i, a, b, d in zip(range(n), A, B, D):
    B[i] = b / a
    D[i] = d / a

