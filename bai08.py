bang_ten = {}
while True:
    name = input()
    tuoi = input()
    if name != "":
        bang_ten[name] = tuoi
    else:
        break
for key, value in bang_ten.items():
    print(f"{key}: {value} tuoi")