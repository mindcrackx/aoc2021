data = open("input.txt", "r", encoding="utf-8").read().splitlines()

oxygen, co2 = "", ""

possibleOxygen = data
possibleCo2 = data
lengthBinary = len(data[0])
for x in range(lengthBinary):

    if len(possibleOxygen) > 1:
        countOxygen = 0
        newPossibleOxygen = []
        for line in possibleOxygen:
            if line[x] == "1":
                countOxygen += 1
        oxygenMostCommon = "1"
        if countOxygen < (len(possibleOxygen) / 2):
            oxygenMostCommon = "0"
        for line in possibleOxygen:
            if line[x] == oxygenMostCommon:
                newPossibleOxygen.append(line)
        possibleOxygen = newPossibleOxygen

    if len(possibleCo2) > 1:
        countCo2 = 0
        newPossibleCo2 = []
        for line in possibleCo2:
            if line[x] == "1":
                countCo2 += 1
        co2LeastCommon = "0"
        if countCo2 < (len(possibleCo2) / 2):
            co2LeastCommon = "1"
        for line in possibleCo2:
            if line[x] == co2LeastCommon:
                newPossibleCo2.append(line)
        possibleCo2 = newPossibleCo2

print(int(possibleOxygen[0], base=2) * int(possibleCo2[0], base=2))
