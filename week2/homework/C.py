stack = []
reg = None
code = input().split()
for inst in code:
    match inst:
        case "+":
            reg = stack.pop() + reg
        case "-":
            reg = stack.pop() - reg
        case "*":
            reg = stack.pop() * reg
        case _:
            stack.append(reg)
            reg = int(inst)

print(reg)
