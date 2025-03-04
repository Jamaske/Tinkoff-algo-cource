import math


def f(x):
    return x ** 2 + math.sqrt(x + 1)

def newton(x, C):
    a = math.sqrt(x + 1)    
    return (2 * ((C + x**2)*a -1) - x)/(4 * x * a + 1)

C = float(input())
if C > 2.4:
    x = math.sqrt(C - math.pow(C, 0.25) - 0.1)
else:
    x = math.sqrt(C - 0.93701171875) - 0.25

while abs(f(x) - C) >  1e-10 * (x + 0.25):
    #print(x)
    x = newton(x, C)
    
print(x)