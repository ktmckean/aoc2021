a = 0
numIncreased = 0

for line in open("./day1input.txt"):
    intLine = int(line)
    if intLine == 0:
        print("This won't work! Handle zeros!")
        exit()
    # We need to load the first number before we can compare.
    if a == 0:
        a = intLine
        continue
    else:
        if intLine > a:
            numIncreased += 1
    a = intLine


print(numIncreased)