s = input()
mang = [int(x) for x in s.split()]
mang_moi = []
for i in mang:
    if i > 10 and i % 2 == 0:
        mang_moi.append(i)
print(mang_moi)