data = open("input.txt", "r", encoding="utf-8").read().splitlines()
data = [int(x) for x in data]

inc = 0
old = data[0] + data[1] + data[2]
for x, y, z in zip(data[1:], data[2:], data[3:]):
    new = x + y + z
    if new > old:
        inc += 1
    old = new

print(inc)
