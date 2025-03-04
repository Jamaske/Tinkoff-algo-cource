input()
a = set(map(int, input().split()))
b = map(int, input().split())
for req in b:
    print("YES" if req in a else "NO")

#O(n+k)