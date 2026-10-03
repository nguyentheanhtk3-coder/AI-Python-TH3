mang = []
while True:
    s = input()
    if s != "":
        mang.append(s)
    else:
        break
dem = {}
for i in mang:
    if i in dem:
        dem[i] += 1
    else:
        dem[i] = 1
for key, value in dem.items():
    print(f"{key}: {value}")