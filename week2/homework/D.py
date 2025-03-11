
input()
inp = map(int, input().split())
stack:list[tuple[int, int]] = []
cnt = 0
cur = None
score = 0
for el in inp:
    if cur == el: 
        cnt += 1
    else:
        if cnt < 3:
            stack.append((cur, cnt))
        else:
            score += cnt
        cur = el
        cnt = 1
        if stack[-1][0] == cur:
            cnt += stack.pop()[1]

if cnt>=3:
    score += cnt

print(score)
