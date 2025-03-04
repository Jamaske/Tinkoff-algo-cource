from sys import stdin

stack: list[int] = []
minimums: list[int] = []
minimum: int = 2**63 - 1

n = int(input())

results = []


for _ in range(n):
    inst = next(stdin)
    #print(len(inst))
    if len(inst) > 2: 
        val = int(inst[2:])
        stack.append(val)
        if val <= minimum:
            minimums.append(minimum)
            minimum = val

        continue
    if inst == "2\n": # pop
        if minimum == stack.pop():
            minimum = minimums.pop()

    else: # max
        results.append(str(minimum))


print("\n".join(results))

        
