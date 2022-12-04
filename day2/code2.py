with open('/Users/freddiejonas/Documents/GitHub/AdventOfCode2022/day2/input.txt') as f:
    contents = f.read()
    array = contents.split('\n')
    totalSum = 0
    for item in array:
        try:
            score = 0
            print(item[0] + "-" + item[2])
            if item[0] == 'A': # rock
                if item[2] == "X": # lose
                    score += 0 + 3
                if item[2] == "Y": # draw
                    score += 3 + 1
                if item[2] == "Z": # win
                    score += 6 + 2
            if item[0] == 'B': # paper
                if item[2] == "X":
                    score += 0 + 1
                if item[2] == "Y":
                    score += 3 + 2
                if item[2] == "Z":
                    score += 6 + 3
            if item[0] == 'C': # scissors
                if item[2] == "X":
                    score += 0 + 2
                if item[2] == "Y":
                    score += 3 + 3
                if item[2] == "Z":
                    score += 6 + 1
            totalSum += score
            continue
        except:
            continue


    print(totalSum)