s = input()
mang = [int(x) for x in s.split()]
dem = {}
mang_moi = []
for i in mang:
    if i not in dem:
        dem[i] = 1
        mang_moi.append(i)
print(mang_moi)