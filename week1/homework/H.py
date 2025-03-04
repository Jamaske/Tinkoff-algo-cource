n = int(input())
count = [0] * 26
s = input()
for ch in s:#count
    
    count[ord(ch) - 0x41] += 1

half = []
singular = ''
for code, cnt in enumerate(count):
    p = cnt >> 1
    if p:
        half.append(str(chr(code + 0x41)) * p)
    if not singular and cnt & 1:
        singular = chr(code + 0x41)

first_half = ''.join(half)
second_half = ''.join(half[::-1])


print(first_half + singular + second_half)



