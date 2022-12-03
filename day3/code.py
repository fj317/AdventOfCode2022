from calendar import c
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

with open('/Users/freddiejonas/Documents/GitHub/AdventOfCode2022/day3/input.txt') as f:
    contents = f.read()
    input = contents.split('\n')
    sum = 0
    for rucksack in input[:-1]:
        compartmentOne, compartmentTwo = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        matchedItem = ''.join(set(compartmentOne) & set(compartmentTwo))
        priority = characters.index(matchedItem) + 1
        sum += priority
    print(sum)