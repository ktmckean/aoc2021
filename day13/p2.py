def readInput():
	afterTheBreak = False
	dots = []
	instructions = []
	for line in open("input.txt"):
		if line == '\n':
			afterTheBreak = True
			continue
		
		line = line.strip()
		if not afterTheBreak:
			coord = []
			for num in line.split(','):
				coord.append(int(num))
			dots.append(coord)
		
		else:
			instructions.append(line)
	return dots,instructions

def foldAlongLine(xy, val, dots):
	if xy == 'x':
		return foldHorizontal(dots,val)
	elif xy == 'y':
		return foldVertical(dots,val)
	else:
		print("error: must fold x or y")
		
def foldHorizontal(dots, crease):
	newDots = []
	for pt in dots:
		x = pt[0]
		y = pt[1]
		if y < crease:
			if [x,y] not in newDots:
				newDots.append([x,y])
		elif y > crease:
			newy = crease - abs(y - crease)
			if [x,newy] not in newDots:
				newDots.append([x,newy])
			if newy > crease or newy < 0:
				print("Error: bottom half is bigger!")
				exit()
		else:
			# dist == 0
			print("error! dot found on crease")
	return newDots
	
def foldVertical(dots, crease):
	newDots = []
	for pt in dots:
		x = pt[0]
		y = pt[1]
		if x < crease:
			if [x,y] not in newDots:
				newDots.append([x,y])
		elif x > crease:
			newx = crease - abs(x - crease)
			if [newx,y] not in newDots:
				newDots.append([newx,y])
			if newx > crease or newx < 0:
				print("Error: bottom half is bigger!")
				exit()
		else:
			# dist == 0
			print("error! dot found on crease")
	return newDots


'''
def foldHorizontal2(dots,crease):
	numDistinct = {}
	for pt in dots:
		if crease > pt[0]:
				
			if not numDistinct[pt[1]]:
				numDistinct[pt[1]] = 


def countFoldedPts(dots, crease):
	foldedPts = {}
	for pt in dots:
		newy = abs(crease - pt[1])
		x = pt[0]
		if x in foldedPts.keys():
			foldedPts[x].add(newy)
		else:
			foldedPts[x] = {newy}
	
	sum = 0
	#print(foldedPts)
	for ys in foldedPts.values():
		sum += len(ys)
	return sum
'''

def parseInstructions(instructions):
	orders = []
	for line in instructions:
		coord = line.split('=')
		orders.append([coord[0][-1], int(coord[1])])		
	return orders

dots,instructions = readInput()
folds = parseInstructions(instructions)
for fold in folds:
	if fold[0] == 'x':
		print("folding vertical around "+str(fold[1]))
		dots = foldVertical(dots, fold[1])
	elif fold[0] == 'y':
		print("folding horizontal around "+str(fold[1]))
		dots = foldHorizontal(dots, fold[1])

xmax = 0
ymax = 0
for dot in dots:
	if dot[0] > xmax:
		xmax = dot[0]
	if dot[1] > ymax:
		ymax = dot[1]

grid = [['.' for i in range(xmax+1)] for j in range(ymax+1)]

for dot in dots:
	grid[dot[1]][dot[0]] = '#'
print(grid)