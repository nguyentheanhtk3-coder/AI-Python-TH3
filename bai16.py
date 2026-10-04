danh_sach = {}
while True:
    name = input()
    if name == "":
        break
    diem = int(input())
    danh_sach[name] = diem
danh_sach = dict(sorted(danh_sach.items(), key=lambda x: x[1], reverse=True))
for name, diem in danh_sach.items():
    print(f"{name}: {diem}")