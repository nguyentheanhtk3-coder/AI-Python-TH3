mang = input().split()
mang_nguoc = []
for i in range(len(mang)-1, -1, -1):
    mang_nguoc.append(mang[i])
print(mang_nguoc)