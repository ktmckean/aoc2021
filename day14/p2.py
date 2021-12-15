def readInput():
	start = ""
	rules = {}
	for line in open("input.txt"):
		if line == '\n':
			continue
		line = line.strip()

		if '->' not in line:
			start = line
		else:
			rule = line.split(' -> ')
			rules[rule[0]] = rule[1]
	return start, rules

def updateString(start, rules):
	newString = ""
	for i,char in enumerate(start):
		if i+1 == len(start):
			newString += char
			break

		segment = char + start[i+1]
		insert = rules[segment]
		newString += char + insert
	return newString

def updateStringManyTimes(string,rules,numIterations):
	newString = string
	for i in range(numIterations):
		newString = updateString(newString,rules)
	return newString

def getCharCounts(string):
	counts = {}
	for char in string:
		if char not in counts.keys():
			counts[char] = 1
		else:
			counts[char] += 1
	return counts

'''
def runCycle(pair,rules):
	s = ""
	newPair = pair
	count = 0
	while True:
		s += rules[newPair]
		newPair = pair[0] + s[-1]
		count += 1

		if newPair == pair:
			break

def getCycleLength(pair,rules):
	new = rules[pair]
	count = 1
	lastNew = pair[1]
	while new != lastNew:
		count += 1
		lastNew = new
		new = rules[(pair[0] + new)]

	return count

def getAllCycleLengths(string,rules):
	lengths = {}
	for i,char in enumerate(string):
		if i+1 == len(string):
			break
		pair = char + string[i+1]
		lengths[pair] = getCycleLength(pair,rules)

	return lengths

def getReturnTimes(rules):
	times = {}
	for key in rules:
		newKey = key
		time = 0
		sequence = key[1]
		newChar = ''
		while True:
			newChar = rules[newKey]
			time += 1
			if newChar not in sequence:
				sequence += newChar
				newKey = key[0] + newChar
			else:
				break

		times[key] = [sequence.index(newChar), time]
	return times
'''

def getPairCounts(string,rules):
	pairs = {}
	for i,c in enumerate(string):
		if i+1 == len(string):
			break
		pair = c + string[i+1]
		if pair not in pairs.keys():
			pairs[pair] = 1
		else:
			pairs[pair] += 1
	return pairs

def updatePairCountsOneStep(pairCounts,rules):
	pairs = {}
	for pair in pairCounts.keys():
		pairs[pair] = 0

	for pair in pairCounts.keys():
		infix = rules[pair]
		newPair1 = pair[0] + infix
		newPair2 = infix + pair[1]

		for new in [newPair1,newPair2]:
			if new not in pairs.keys():
				pairs[new] = pairCounts[pair]
			else:
				pairs[new] += pairCounts[pair]
	return pairs


def getPairCountsAfterManySteps(string, rules, numSteps):
	pairCounts = getPairCounts(string,rules)
	for i in range(numSteps):
		pairCounts = updatePairCountsOneStep(pairCounts, rules)
	return(pairCounts)

def getLetterCountsFromPairCounts(counts,originalString):
	letterCounts = {}
	for pair in counts.keys():
		letterCounts[pair[0]] = 0
		letterCounts[pair[1]] = 0

	for pair in counts.keys():
		#print(pair,counts[pair])
		letterCounts[pair[0]] += counts[pair]
		letterCounts[pair[1]] += counts[pair]
		
	letterCounts[originalString[0]] -= 1
	letterCounts[originalString[-1]] -= 1
	
	for l in letterCounts.keys():
		assert(letterCounts[l] % 2 == 0)
		letterCounts[l] = int(letterCounts[l] / 2)

	letterCounts[originalString[0]] += 1
	letterCounts[originalString[-1]] += 1
	
	return letterCounts

def getMaxAndMinLetterCounts(counts):
	max = 0
	min = -1
	for count in counts.values():
		if count > max:
			max = count
		if min==-1 or count < min:
			min = count
	return max,min


string,rules = readInput()

pairCounts = getPairCounts(string,rules)

pairCounts = getPairCountsAfterManySteps(string, rules, 40)
#print(pairCounts)
letterCounts = getLetterCountsFromPairCounts(pairCounts, string)
#print(letterCounts)
max,min = getMaxAndMinLetterCounts(letterCounts)

print(max, min)
print(max - min)


#print(getCycleLength('KO',rules))

#print(lengths)