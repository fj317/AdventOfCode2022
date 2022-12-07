with open('/Users/freddiejonas/Documents/GitHub/AdventOfCode2022/day6/input.txt') as f:
    contents = f.read()
    char1 = contents[0]
    char2 = contents[1]
    char3 = contents[2]
    char4 = contents[3]

    for i in range(3, len(contents)-1):
        char1 = contents[i-3]
        char2 = contents[i-2]
        char3 = contents[i-1]
        char4 = contents[i]
        buffer = set((char1, char2, char3, char4))
        if len(buffer) == 4:
            print(i+1)
            break
