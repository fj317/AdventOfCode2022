with open('/Users/freddiejonas/Documents/GitHub/AdventOfCode2022/day4/input.txt') as f:
    contents = f.read()
    input = contents.split('\n')
    count = 0
    for row in input[:-1]:
        assignmentSections = set()
        sections = row.split(',')
        elf1 = sections[0].split('-')
        elf2 = sections[1].split('-')
        for i in range(int(elf1[0]), int(elf1[1])+1):
            assignmentSections.add(i)
        for i in range(int(elf2[0]), int(elf2[1])+1):
            if i in assignmentSections:
                count+=1
                break
    print(count)