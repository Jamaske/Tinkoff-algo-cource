

def inc(number: list) -> None:
    depth = 0
    while number and number[-1]:
        depth += 1
        number.pop()

    if not number:# достали все знаки
        number.append(True)
    else:
        number.pop()# достали первый ноль
        number.append(True) # заменили еденицей
    
    while depth:
        number.append(False)
        depth -= 1
        

def toBin(number):
    for bit in number:print(int(bit), end='')
    print()

number = []

for i in range(10):

    inc(number)
    toBin(number)



# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111