dic1 = {}
dic2 = {}
while True:
    key = input()
    if key == "":
        break
    value = input()
    dic1[key] = value

while True:
    key = input()
    if key == "":
        break
    value = input()
    dic2[key] = value
for key,value in dic1.items():
    if key in dic2:
        dic2[key] += value
    else:
        dic2[key] = value

for key, value in dic2.items():
    print(f"{key}: {value}")