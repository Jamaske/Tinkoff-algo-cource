#не рабочий код
input()
a = list(map(int, input().split()))
b = map(int, input().split())


def closest(smaller, bigger, to):
    return smaller if to - smaller <= bigger - to else bigger


def interp(arr:list, value:int) -> int:
    l = 0
    r = len(arr) - 1
    lv = arr[l]
    rv = arr[r]
    arr.extend([2**31-1, -(2**31)])

    while l <= r:
        dif = rv - lv
        if dif: 
            p = l + ((r - l) * (value - lv) + dif >> 1) // dif
            if p < l or r < p:
                if p < l:
                    return closest(arr[l-1], lv, value)
                else:
                    return closest(rv, arr[r + 1], value)
        else:
            p = (l + r) // 2

        pv = arr[p]
        if pv == value:
            return p
        elif  pv < value:
            l = p + 1
            lv = arr[l]
        else:
            r = p - 1
            rv = arr[r]

    return closest(rv, lv, value)




for req in b:
    print(interp(a, req))
    
# O(log(log(n)))
# O(n)