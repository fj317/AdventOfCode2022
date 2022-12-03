from calendar import c

with open('/Users/freddiejonas/Documents/GitHub/AdventOfCode2022/day2/input.txt') as f:
    contents = f.read()
    array = contents.split('\n');
    totalSum = 0
    for item in array:
        try:
            score = 0
            print(item[0] + "-" + item[2])
            if item[0] == 'A':
                if item[2] == "X":
                    score += 1 + 3
                if item[2] == "Y":
                    score += 2 + 6
                if item[2] == "Z":
                    score += 3 + 0
            if item[0] == 'B':
                if item[2] == "X":
                    score += 1 + 0
                if item[2] == "Y":
                    score += 2 + 3
                if item[2] == "Z":
                    score += 3 + 6
            if item[0] == 'C':
                if item[2] == "X":
                    score += 1 + 6
                if item[2] == "Y":
                    score += 2 + 0
                if item[2] == "Z":
                    score += 3 + 3
            totalSum += score
            continue
        except:
            continue


    print(totalSum)