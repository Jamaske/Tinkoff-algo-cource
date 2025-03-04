
def sort(arr:list):
    end = len(arr)
    invers = 0
    for i in range(0, end-1,2):
        if arr[i+1] < arr[i]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            invers += 1
    
    axil = [None] * end
    size = 2
    while size < end:
        for i in range(0, end - size, size << 1):
            k = i
            j = i_e = i + size
            j_e = min(j + size, end)
            local_inv = 0
            while i < i_e and j < j_e:
                if arr[i] < arr[j]:
                    axil[k] = arr[i]
                    i += 1
                    local_inv += j
                else:
                    axil[k] = arr[j]
                    j += 1
                k += 1
            while i < i_e:
                axil[k] = arr[i]
                i += 1
                k += 1
                local_inv += j
            while j < j_e:
                axil[k] = arr[j]
                j += 1
                k += 1
           
            invers += local_inv - i_e * size
        while k < end:
            axil[k] = arr[k]
            k += 1
        arr, axil = axil, arr
        size *= 2
    return invers, arr

def bubl(arr):
    l = len(arr)
    inv = 0
    for i in range(l-1, 0, -1):
        for j in range(0, i):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                inv += 1
    return inv, arr

input()
a = list(map(int, input().split()))
inv, a = sort(a)

print(inv, ' '.join(map(str,a)), sep='\n')
