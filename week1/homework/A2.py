input()
a = list(map(int, input().split()))
b = map(int, input().split())

def search(arr: list, val: int) -> int:
    l = 0
    r = len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] < val:
            l = m + 1
        else:
            r = m
    return l


for req in b:
    print("YES" if a[search(a, req)] == req else "NO")

#O(k*log(n))