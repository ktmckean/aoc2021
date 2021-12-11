perens = 0
squares = 0
braces = 0
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
	