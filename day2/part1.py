data = open("input.txt", "r", encoding="utf-8").read().splitlines()

horizontal, depth = 0, 0
for line in data:
    cmd, num = line.split(" ")
    num = int(num)
    if cmd == "forward":
        horizontal += num
    elif cmd == "down":
        depth += num
    elif cmd == "up":
        depth -= num

print(horizontal * depth)
