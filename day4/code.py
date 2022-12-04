from multiprocessing.reduction import duplicate

with open('/Users/freddiejonas/Documents/GitHub/AdventOfCode2022/day4/input.txt') as f:
    contents = f.read()
    input = contents.split('\n')
    contents = []
    assignmentSections = set()
    duplicateCount = 0
    for row in input[:-1]:
        sections = row.split(',')
        contents.append(sections[0].split('-'))
        contents.append(sections[1].split('-'))

    for section in contents:
        for i in range(int(section[0]), int(section[1])+1):
            if i in assignmentSections:
                print(i)
                print(assignmentSections)
                duplicateCount += 1
            else:
                assignmentSections.add(i)

    print(duplicateCount)
    # splitInput = input.split(',')
    # print(contents)
    # for section in splitInput:
    #     print(section)
    #     splitSections = []
    #     splitSections = section.split('-')
    #     print(splitSections)
