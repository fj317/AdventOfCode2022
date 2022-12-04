with open('/Users/freddiejonas/Documents/GitHub/AdventOfCode2022/day4/input.txt') as f:
    contents = f.read()
    input = contents.split('\n')
    count = 0
    for row in input[:-1]:
        sections = row.split(',')
        elf1 = sections[0].split('-')
        elf2 = sections[1].split('-')
        print(sections)
        elf1a = int(elf1[0])
        elf1b = int(elf1[1])
        elf2a = int(elf2[0])
        elf2b = int(elf2[1])

        if (elf2a <= elf1a) and (elf2b >= elf1b) or (elf1a <= elf2a) and (elf1b >= elf2b):
            count+=1
            print('here')
    print(count)