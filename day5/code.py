def printList(list):
    for item in list:
        print(item)

with open('/Users/freddiejonas/Documents/GitHub/AdventOfCode2022/day5/input.txt') as f:
    contents = f.read()
    input = contents.split('\n')
    stacks = [[],[],[],[],[],[],[],[],[]]
    for i in range(7, -1, -1):
        for j in range(1, len(input[0]), 4):
            char = input[i][j]
            if (char != ' '):
                stacks[(j-1)/4].append(char);

    instructions = input[10:]
    numberOfCratesToMove = 0
    fromStack = 0
    toStack = 0

    for instruction in instructions[:-1]:
        splitInstruction = instruction.split(' ');
        numberOfCratesToMove = int(splitInstruction[1])
        fromStack = int(splitInstruction[3]) - 1
        toStack = int(splitInstruction[5]) - 1
        for i in range (0, numberOfCratesToMove):
            if stacks[fromStack]:
                stacks[toStack].append(stacks[fromStack].pop())

        
    printList(stacks)
