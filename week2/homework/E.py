stack = []

input()
inbound = map(int, input().split())
requiered_cart = 1
ans = []
for cart in inbound:
    ans.append("1 1")
    if cart != requiered_cart:
        stack.append(cart)
        continue
    
    # cart == req -> depart the cart
    ans.append("2 1")
    requiered_cart += 1

    while stack and stack[-1] == requiered_cart:
        ans.append("2 1")
        requiered_cart += 1
        stack.pop()

if stack:
    print(0)
else:
    print(len(ans))
    print('\n'.join(ans))
