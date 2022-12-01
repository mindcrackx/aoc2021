data = open("input.txt", "r", encoding="utf-8").read().splitlines()
data = [int(x) for x in data]

inc = 0
for x, y in zip(data, data[1:]):
    if x < y:
        inc += 1

print(inc)
