from calendar import c

with open('/Users/freddiejonas/Documents/GitHub/AdventOfCode2022/day1/input.txt') as f:
    contents = f.read()
    array = contents.split('\n');
    sumValues = [];
    total = 0
    for item in array:
        try: 
            total += int(item)
            continue
        except:
            sumValues.append(total)
            total = 0
            continue

    print(max(sumValues))
    sumValues.sort(reverse=True)
    maxTotal = sumValues[0]+sumValues[1]+sumValues[2]
    print(maxTotal);

print("El Fin")