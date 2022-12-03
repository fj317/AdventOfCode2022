from calendar import c
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

with open('/Users/freddiejonas/Documents/GitHub/AdventOfCode2022/day3/input.txt') as f:
    contents = f.read()
    input = contents.split('\n')
    sum = 0
    for i in range(0, len(input) - 1, 3):
        teamMatchItem = ''.join(set(input[i]) & set(input[i+1]) & set(input[i+2]))
        priority = characters.index(teamMatchItem) + 1
        sum += priority
    print(sum)