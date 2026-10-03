s = input()
mang = [int(x) for x in s.split()]
maxn = 0
for i in mang:
    n = mang.count(i)
    if n > maxn:
        maxn = n
        max_value = i
print(max_value)