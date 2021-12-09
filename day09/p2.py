import copy

def readInput():
	heights = []
	for line in open("input.txt"):
		row = []
		line = line.strip()
		for char in line:
			row.append(int(char))
		heights.append(row)
	return heights

def isLowPoint(x,y, heights):
	if x != 0 and 					heights[x-1][y] <= heights[x][y]:
		return False
	if x != len(heights)-1 and 		heights[x+1][y] <= heights[x][y]:
		return False
	if y != 0 and 					heights[x][y-1] <= heights[x][y]:
		return False
	if y != len(heights[x])-1 and 	heights[x][y+1] <= heights[x][y]:
		return False
	print(x,y,heights[x][y])
	return True

def getMinima(heights):
	# x and y are reverse their normal meaning
	minima = []
	for x in range(len(heights)):
		for y in range(len(heights[x])):
			if isLowPoint(x,y,heights):
				minima.append([x,y])
	return minima

def sumRiskLevels(heights):
	minima = getMinima(heights)
	cumSum = 0	
	for xy in minima:
		cumSum += heights[xy[0]][xy[1]] + 1
	return cumSum

def flattenBasins(heights):
	flats = copy.deepcopy(heights)
	for x,row in enumerate(heights):
		for y,num in enumerate(row):
			if num != 9:
				flats[x][y] = 0
	return flats

def exploreBasinRecursive(x,y,basins):
	if basins[x][y] == 9 or basins[x][y] == 1:
		return basins,0
	
	assert(basins[x][y] == 0)
	basins[x][y] = 1
	
	size1 = 0
	size2 = 0
	size3 = 0
	size4 = 0
	
	if x > 0:
		basins,size1 = exploreBasinRecursive(x-1,y,basins)
	if x < len(basins)-1:
		basins,size2 = exploreBasinRecursive(x+1,y,basins)
	if y > 0:
		basins,size3 = exploreBasinRecursive(x,y-1,basins)
	if y < len(basins[x])-1:
		basins,size4 = exploreBasinRecursive(x,y+1,basins)
	
	size = 1
	size += size1
	size += size2
	size += size3
	size += size4
	return basins,size	

def exploreBasins(heights):
	basins = flattenBasins(heights)
	basinSizes = []
	for x,row in enumerate(basins):
		for y,num in enumerate(row):
			if num == 0:
				basins,size = exploreBasinRecursive(x,y,basins)
				basinSizes.append(size)
	return basinSizes

#def exploreNeighbors(x,y,basins,coordsToExplore):


def exploreBasinLoop(x,y,basins):
	assert(basins[x][y] == 0)
	
	coordsToExplore = [[x,y]]
	size = 0
	while len(coordsToExplore) != 0:
		x = coordsToExplore[0][0]
		y = coordsToExplore[0][1]
		basins[x][y] = 1
		size += 1
		coordsToExplore.remove([x,y])
		
		if x > 0 				and basins[x-1][y] == 0:
			coordsToExplore.append([x-1,y])
			
		if x < len(basins)-1 	and basins[x+1][y] == 0:
			coordsToExplore.append([x+1,y])
			
		if y > 0  				and basins[x][y-1] == 0:
			coordsToExplore.append([x,y-1])
			
		if y < len(basins[x])-1 and basins[x][y+1] == 0:
			coordsToExplore.append([x,y+1])
	return basins,size
			
def exploreBasinsWithLoop(heights):
	basins = flattenBasins(heights)
	basinSizes = []
	for x,row in enumerate(basins):
		for y,num in enumerate(row):
			if num == 0:
				basins,size = exploreBasinLoop(x,y,basins)
				basinSizes.append(size)
	return basinSizes

def getMax3Product(basinSizes):
	maxProduct = 1
	for i in range(3):
		m = max(basinSizes)
		maxProduct *= m
		basinSizes.remove(m)
	return maxProduct

heights = readInput()
basinSizes = exploreBasins(heights)
basinSizes2 = exploreBasinsWithLoop(heights)

maxProduct = getMax3Product(basinSizes)
print(getMax3Product(basinSizes))
maxProduct2 = getMax3Product(basinSizes2)
print(getMax3Product(basinSizes2))


	
print(maxProduct)
