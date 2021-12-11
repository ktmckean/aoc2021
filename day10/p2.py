score = 0

stack = []
input = open("input.txt").readlines()

for line in open("input.txt"):
	for char in line:
		if char == '\n':
			continue
		if char == '(' or char == '[' or char == '{' or char == '<':
			stack.append(char)
		else:
			last = stack.pop()
			corrupt = False
			
			if char == ')' and last != '(':
				score += 3	
				corrupt = True
			if char == ']' and last != '[':
				score+= 57
				corrupt = True
			if char == '}' and last != '{':
				score += 1197
				corrupt = True
			if char == '>' and last != '<':
				score += 25137
				corrupt = True
			
			if corrupt == True:
				stack = []
				input.remove(line)
				break
				
print(score)

scores2 = []
for line in input:
	for char in line:
		if char == '\n':
			continue
		if char == '(' or char == '[' or char == '{' or char == '<':
			stack.append(char)
		else:
			last = stack.pop()
	
	linescore = 0
	while len(stack) > 0:
		last = stack.pop()
			
		linescore *= 5
		if last == '(':
			linescore += 1
		if last == '[':
			linescore += 2
		if last == '{':
			linescore += 3
		if last == '<':
			linescore += 4
	scores2.append(linescore)

midpoint = int((len(scores2)-1)/2)
print(sorted(scores2)[midpoint])