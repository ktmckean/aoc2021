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
	
	
	
	
	
	
string,rules = readInput()
print(string)
for i in range(10):
	string = updateString(string,rules)
	print(string)

counts = {}
for char in string:
	if char not in counts.keys():
		counts[char] = 1
	else:
		counts[char] += 1
print(counts)