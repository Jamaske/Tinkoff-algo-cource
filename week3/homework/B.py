from sys import stdin
from itertools import islice
N, root = map(int, input().split())
childs = [tuple(map(lambda x: int(x) if x != '-1' else None,  input().split())) for _ in range(N)]

#print(childs)

ret_reg = None
stack = [[root, -1e10, 1e10, None]]
while stack:
    cur, low, high, ret_var = stack[-1]
    if ret_reg is None: # enter the farame via call from parent
        if cur is None:
            ret_reg = 0
            stack.pop()
            continue

        if cur <= low or high <= cur: 
            print(0)
            break

        left, _ = childs[cur]
        ret_reg = None
        stack.append([left, low, cur, None])

    elif ret_var is None: # enter the frame via return from left
        stack[-1][3] = ret_reg

        _, right = childs[cur]
        ret_reg = None
        stack.append([right, cur, high, None])

    else: # enter the frame via return from right
        if ret_var > ret_reg + 1 or ret_var + 1 < ret_reg:
             print(0)
             break
        ret_reg = 1 + max(ret_reg, ret_var)
        stack.pop()
else:
        print(1)