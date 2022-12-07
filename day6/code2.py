with open('/Users/freddiejonas/Documents/GitHub/AdventOfCode2022/day6/input.txt') as f:
    contents = f.read()

    for i in range(14, len(contents)-1):
        chars = []
        for j in range (14, 0, -1):
            chars.append(contents[i-j])
        buffer = set(chars)
        if len(buffer) == 14:
            print(i)
            break
