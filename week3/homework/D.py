data = [1_000_000_000, -1_000_000_000]
size = 0
N = int(input())
for _ in range(N):
    inst = input()
    if len(inst) == 1:# pop
        ret = data[1]
        val = data[size]
        idx = 1
        size -= 1
        if idx > size:
            print(ret)
            continue
        
        while idx * 2 <= size:
            
            ch = 2 * idx
            if data[ch] < data[ch + 1]:
                ch += 1
            
            if data[ch] > val:
                data[idx] = data[ch]
                idx = ch
            else:
                break
            
        data[idx] = val
        print(ret)

    else:
        val = int(inst[2:])
        size += 1
        if size == len(data) - 1:
            data.append(-1_000_000_000)

        #seve up
        idx = size
        while idx and val > data[idx // 2]:
            data[idx] = data[idx//2]
            idx = idx//2
        data[idx] = val
        
