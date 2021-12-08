def readInput():
	signals = []
	outputs = []

	for line in open("input.txt"):
		line = line.strip()
		patternStr,outputStr = line.split(" | ")
		signals.append(patternStr.split(" "))
		outputs.append(outputStr.split(" "))
	
	return signals,outputs

def getSignalCodes(signal):
	codes = {}
	twoDarks = []
	oneDarks = []
	for code in signal:
		size = len(code)
		if size == 2:
			codes[1] = code
		elif size == 3:
			codes[7] = code
		elif size == 4:
			codes[4] = code
		elif size == 7:
			codes[8] = code
		elif size == 6:
			oneDarks.append(code)
		elif size == 5:
			twoDarks.append(code)
	codes.update(decodeOneDarks(oneDarks, codes))
	codes.update(decodeTwoDarks(twoDarks, codes))
	
	return codes

# "known" must contain a code for 7
def isThisSix(sixCode, known):
	sevenCode = known[7]
	for char in sevenCode:
		if char not in sixCode:
			return True
	return False

# "known" must contain a code for 4	
def isThisZero(zeroCode, known):
	fourCode = known[4]
	for char in fourCode:
		if char not in zeroCode:
			return True
	return False

# one darks contains codes for 0, 6, and 9
# known contains codes for 7 and 4
def decodeOneDarks(oneDarks, known):
	newCodes = {}
	for code in oneDarks:
		if isThisSix(code, known):
			newCodes[6] = code
		elif isThisZero(code, known):
			newCodes[0] = code
		else:
			newCodes[9] = code
	return newCodes
	
# "known" must contain a code for 9
def isThisTwo(twoCode, known):
	nineCode = known[9]
	for char in twoCode:
		if char not in nineCode:
			return True
	return False

# "known" must contain a code for 7	
def isThisThree(threeCode, known):
	sevenCode = known[7]
	for char in sevenCode:
		if char not in threeCode:
			return False
	return True

#twoDarks contains codes for 2, 3, and 5
#known contains codes for 7 and 9
def decodeTwoDarks(twoDarks, known):
	newCodes = {}
	for code in twoDarks:
		if isThisTwo(code, known):
			newCodes[2] = code
		elif isThisThree(code, known):
			newCodes[3] = code
		else:
			newCodes[5] = code
	return newCodes

def decodeOutput(output, codes):
	num = 0
	for digit in output:
		digitSet = set(digit)
		for codeNum,codeStr in codes.items():
			codeSet = set(codeStr)
			if codeSet == digitSet:
				num *= 10
				num += codeNum
				break
	return num
	

signals, outputs = readInput()

cumSum = 0
for index,signal in enumerate(signals):
	codes = getSignalCodes(signal)
	cumSum += decodeOutput(outputs[index], codes)
print(cumSum)	

	
