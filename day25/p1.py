def readInput():
	grid = []
	for line in open('input.txt'):
		line = line.strip()
		row = []
		for c in line:
			row.append(c)
		grid.append(row)
	return grid
	
def moveEast(grid):
	#print(grid)
	numMoved = 0
	easts = [ ['.' for x in range(len(grid[0]))] for y in range(len(grid))]
	for y,row in enumerate(grid):
		for x,c in enumerate(row):
			if easts[y][x] == '>':
				#print('1')
				#this only happens if we moved something in already
				# which only happens when grid[y][x] is a '.'
				#so there is definitely nothing left to do here
				continue
			
			if c != '>' :
				#print('2')
				#leave it as a '.'
				continue

			next = (x+1) % len(row)
			nextChar = grid[y][next]
			if nextChar == '.':
				#print('3')
				#easts[y][x] = '.'	#already taken care of
				easts[y][next] = '>'
				numMoved += 1
			else:
				#print('4',x,next,nextChar)
				easts[y][x] = '>'
	return easts,numMoved

def mergeGrids(easts,grid):
	#print(easts, grid)
	merged = [ ['.' for x in range(len(grid[0]))] for y in range(len(grid))]
	for y,row in enumerate(grid):
		for x,c in enumerate(row):
			if easts[y][x] == '>':
				#print(easts,grid,x,y)
				assert(c == '.' or c=='>')
				merged[y][x] = '>'
			else:
				if c == 'v':
					merged[y][x] = 'v'
				else:
					merged[y][x] = '.'
	return merged
	
def moveSouth(grid):
	newGrid = [ ['.' for x in range(len(grid[0]))] for y in range(len(grid))]
	numMoved = 0
	for y,row in enumerate(grid):
		for x,c in enumerate(row):
			if newGrid[y][x] == 'v':
				#print('1')
				#this only happens if we moved something in already
				# which only happens when grid[y][x] is a '.'
				#so there is definitely nothing left to do here
				continue
			if grid[y][x]!= 'v':
				#print('2')
				newGrid[y][x] = c
				continue
			
			next = (y+1) % len(grid)
			#print(y,next)
			nextChar = grid[next][x]
			if nextChar != '.':
				#print('3')
				newGrid[y][x] = 'v'
			else:
				#print('4')
				# newGrid[y][x] = '.' #done in initialization
				newGrid[next][x] = 'v'
				numMoved += 1
	return newGrid,numMoved
				
def updateStep(grid):
	numMoved = 0
	easts,numEast = moveEast(grid)
	merged = mergeGrids(easts,grid)
	moved,numSouth = moveSouth(merged)
	return moved,numEast,numSouth
	
def writeGrid(grid):
	s = ''
	for row in grid:
		for c in row:
			s += c
		s += '\n'
	s += '\n'
	open('output.txt','a').write(s)
	
grid = readInput()
f = open('output.txt','w')
f.close()
writeGrid(grid)


c = 0
while True:
	newGrid,me,ms = updateStep(grid)
	#print(me,ms)
	#print(newGrid)

	writeGrid(newGrid)
	c += 1
	if grid == newGrid:
		#print(grid)
		#print(newGrid)
		print(c)
		exit()
	grid = newGrid
	#print(c)

	