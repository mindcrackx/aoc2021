data = open("input.txt", "r", encoding="utf-8").read().splitlines()

horizontal, depth, aim = 0, 0, 0
for line in data:
    cmd, num = line.split(" ")
    num = int(num)
    if cmd == "forward":
        horizontal += num
        depth += aim * num
    elif cmd == "down":
        aim += num
    elif cmd == "up":
        aim -= num

print(horizontal * depth)
