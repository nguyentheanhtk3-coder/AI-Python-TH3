s = input()
mang = s.split()
danh_sach = {}
for i in mang:
    if i in danh_sach:
        danh_sach[i] += 1
    else:
        danh_sach[i] = 1
for key, value in danh_sach.items():
    print(f"{key}: {value}")