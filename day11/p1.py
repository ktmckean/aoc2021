flashes = 0

def readLines():
	grid = []
	for line in open("input.txt"):
		row = []
		for char in line:
			if char == '\n':
				continue
			row.append(int(char))
		grid.append(row)
	return grid

def flashCoord(x,y,flashed,grid):
	if flashed[x][y]:
		return grid
	
	startx = max(x-1,0)
	endx = min(x+1,len(grid)-1)
	starty = max(y-1,0)
	endy = min(y+1,len(grid[0])-1)
	
	#print("flashing "+str(x)+","+str(y))
	#print(range(startx,endx), range(starty,endy))
	
	for tx in range(startx, endx+1):
		for ty in range(starty, endy+1):
			#print("updating "+str(tx)+","+str(ty))
			grid[tx][ty] += 1
	return grid

def doOneStep(grid):
	for i,row in enumerate(grid):
		for j,num in enumerate(row):
			grid[i][j] += 1
	
	flashed = [[False for i in range(len(grid[0]))] for j in range(len(grid))]	
	nines = True
	while(nines):
		nines = False
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if not flashed[i][j] and grid[i][j] > 9:
					nines = True
					grid = flashCoord(i,j,flashed,grid)
					flashed[i][j] = True
					
	flashes = 0
	for x,row in enumerate(flashed):
		for y,didFlash in enumerate(row):
			if didFlash:
				grid[x][y] = 0
				flashes += 1
			
	return flashes,grid


grid = readLines()
flashes = 0
for i in range(100):
	#print(grid)
	#print(flashes)
	stepFlashes,grid = doOneStep(grid)
	flashes += stepFlashes

print(flashes)
