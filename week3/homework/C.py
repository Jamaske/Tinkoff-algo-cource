N = int(input())
childs = [[] for _ in range(N)]

parent = [None]
parent.extend(map(int,input().split()))

for node, par in enumerate(parent[1:], start=1):
    childs[par].append(node)

levels = [None] * N

levels[0] = 0
stack = [0]
while stack:
    node = stack.pop()
    for ch in childs[node]:
        levels[ch] = levels[node] + 1
        stack.append(ch)
    
#print(levels)
M = int(input())
for _ in range(M):
    u, v = map(int, input().split())
    lev = min(levels[u],levels[v])
    for _ in range(levels[u] - lev):
        u = parent[u]
    
    for _ in range(levels[v] - lev):
        v = parent[v]
    while u != v:
        #print(u,v)
        u = parent[u]
        v = parent[v]
    
    print(u)
