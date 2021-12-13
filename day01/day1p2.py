def sumWindow(windowList):
    sum = 0
    for num in windowList:
        sum += num
    return sum


window = []
numIncreased = 0


for line in open("./day1input.txt"):
    intLine = int(line)
    #print(window)
    #print(len(window))
    if len(window) != 3:
        window.append(intLine)
        print("added a number") # If I see this more than three times, there's a problem
        continue
    
    
    
    oldSum = sumWindow(window)
    window.pop(0)
    window.append(intLine)
    newSum = sumWindow(window)
    
    if newSum > oldSum:
        numIncreased += 1
        
print(numIncreased)