s = input()
mang = [int(x) for x in s.split()]
n = int(input())
so1 = 0
so2 = 0
mang.sort()
tam_thoi = 0
for i in mang:
    for j in mang:
        tong = i + j
        if tong == n:
            so1 = i
            so2 = j
            break
        elif tam_thoi < tong < n:
            tam_thoi = tong
            so1 = i
            so2 = j
print(so1, so2) 