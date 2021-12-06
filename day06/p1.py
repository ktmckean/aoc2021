file = open("input.txt")
initStr = file.readline()

fishNums = [0,0,0,0,0,0,0,0,0]

for initNum in initStr.split(','):
    fishNums[int(initNum)] += 1
    
for i in range(80):
    noobs = fishNums[0]
    for age in range(len(fishNums)-1):
        fishNums[age] = fishNums[age+1]
    fishNums[6] += noobs
    fishNums[8] = noobs
    
print(fishNums)
print(sum(fishNums))
    