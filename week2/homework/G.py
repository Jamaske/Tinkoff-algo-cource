from collections import deque

first = deque()
second = deque()

N = int(input())
for _ in range(N):
    inst = input()
    match inst[0]:
        case '+':
            first.appendleft(int(inst[2:]))
            if len(first) > len(second):
                second.appendleft(first.pop())
        case '*':
            if len(first) < len(second):
                first.append(int(inst[2:]))
            else:
                second.appendleft(int(inst[2:]))
            
        case '-':
            print(second.pop())
            if len(first) > len(second):
                second.appendleft(first.pop())


