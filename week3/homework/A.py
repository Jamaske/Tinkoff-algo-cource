N = int(input())
childs = [[] for _ in range(N)]
parent = [None]
parent.extend(map(int,input().split()))

for node, par in enumerate(parent[1:], start=1):
    childs[par].append(node)

hights = [0] * N
deepest = None
deepest_deep = 0
stack = [(0,0)]
visited = [False] * N
while stack:
    cur, depth = stack.pop()
    #print(cur, depth)
    hights[cur] = depth
    if deepest_deep < depth:
        deepest_deep = depth
        deepest = cur

    for el in childs[cur]:
        if not visited[el]:
            visited[el] = True
            stack.append((el, depth + 1))
        

from itertools import chain
def BFS(node:int):
    front = [node]
    visited = set(front)
    next_front = []
    depth = -1
    while front:
        for cur in front:
            if (neighbor := parent[cur]) not in visited and neighbor is not None:
                    visited.add(neighbor)
                    next_front.append(neighbor)

            for neighbor in childs[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_front.append(neighbor)
        #print(front, next_front)
        front.clear()
        depth += 1
        front, next_front = next_front, front
    return depth
width = BFS(deepest)

print(f"{deepest_deep} {width}\n{' '.join(map(str, hights))}")

     
