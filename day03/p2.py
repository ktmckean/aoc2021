
def getDigitCounts(linesToCount):
    counts = [[0 for i in range(2)] for j in range(12)]
    for line in linesToCount:
        idx = 0
        for char in line.strip():
            if char == '0':
                counts[idx][0] += 1
            elif char == '1':
                counts[idx][1] += 1
            else:
                print("Error! non-digit character detected")
                print("it was %s", char)
                exit()
            idx += 1
    return counts
    
def getOxyKeptDigits(counts):
    digits = ""
    for digit in counts:
        kept = "1"
        if digit[0] > digit[1]:
            kept = "0"
        digits += kept
    return digits
    
def getCo2KeptDigits(counts):
    digits = ""
    for digit in counts:
        kept = "0"
        if digit[0] > digit[1]:
            kept = "1"
        digits += kept
    return digits

def getOxy():
    oxyLines = set()
    for line in lines:
        oxyLines.add(line)
    
    counts = getDigitCounts(oxyLines)
    digits = getOxyKeptDigits(counts)    
    
    for idx,dummy in enumerate(digits):
        counts = getDigitCounts(oxyLines)
        digits = getOxyKeptDigits(counts)
        for line in lines:
            if line not in oxyLines:
                continue
            if len(oxyLines) == 1:
                return oxyLines
            if line[idx] != digits[idx]:
                oxyLines.remove(line)
    return oxyLines
    
def getCo2():
    co2Lines = set()
    for line in lines:
        co2Lines.add(line)
    
    counts = getDigitCounts(co2Lines)
    digits = getCo2KeptDigits(counts) 
    
    for idx,dummy in enumerate(digits):
        counts = getDigitCounts(co2Lines)
        digits = getCo2KeptDigits(counts) 
        for line in lines:
            if line not in co2Lines:
                continue
            if len(co2Lines) == 1:
                return co2Lines
            if line[idx] != digits[idx]:
                co2Lines.remove(line)
    return co2Lines

def getDecimalFromBinString(binString):
    dec = 0
    for digit in binString:
        dec *= 2
        if digit == "1":
            dec += 1
    return dec

lines = []
for line in open("input.txt"):
    lines.append(line.strip())

#print(getOxy())
#print(getCo2())

oxyDec = getDecimalFromBinString(getOxy().pop())
print(oxyDec)
co2Dec = getDecimalFromBinString(getCo2().pop())
print(co2Dec)

print(oxyDec * co2Dec)
