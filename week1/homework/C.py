from sys import stdout

l = 1
r = int(input())
while l < r:
    m = (l + r + 1) // 2
    print(m)
    stdout.flush()
    if input() == "<":
        r = m - 1
    else:
        l = m 
print(f"! {l}")
stdout.flush()
