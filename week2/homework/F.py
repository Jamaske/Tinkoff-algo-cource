from collections import deque
from sys import stdin


# [id, ticket]
id_dict: dict[int, int] = {}
qu = deque()
ticket_provider = 0
ticket_getherer = 0

N = int(input())
ans = []
for _ in range(N):
    event = next(stdin)
    if len(event) != 2:
        event, param = event.split()
        param = int(param)
    
    match event:
        case "1":# new human
            qu.appendleft(param)
            id_dict[param] = ticket_provider
            ticket_provider += 1
        case "2\n":# human exit
            del id_dict[qu.pop()]
            ticket_getherer += 1
        case "3\n": # inpationce left
            ticket_provider -= 1
            del id_dict[qu.popleft()]
        case "4": # inpation human
            ans.append(str(id_dict[param] - ticket_getherer))
        case "5\n": # next human
            ans.append(str(qu[-1]))

print('\n'.join(ans))



