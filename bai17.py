data = [
    {"name": "A", "score": 7},
    {"name": "B", "score": 9},
    {"name": "A", "score": 8},
]
danh_sach = {}
for i in data:
    if i["name"] in danh_sach:
        danh_sach[i["name"]].append(i["score"])
    else:
        danh_sach[i["name"]] = [i["score"]]
for name, scores in danh_sach.items():
    print(f"{name}: {scores}")