data = open("input.txt", "r", encoding="utf-8").read().splitlines()

gamma, epsilon = "", ""

lengthBinary = len(data[0])
for x in range(lengthBinary):
    count = 0
    for line in data:
        if line[x] == "1":
            count += 1
    gamma += str(int(count > (len(data) / 2)))
    epsilon += str(int(count < (len(data) / 2)))

print(int(gamma, base=2) * int(epsilon, base=2))
