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
		

heights = []

for line in open("input.txt"):
	row = []
	line = line.strip()
	for char in line:
		row.append(int(char))
	heights.append(row)
	
# x and y are reverse their normal meaning
minima = []
for x in range(len(heights)):
	for y in range(len(heights[x])):
		if isLowPoint(x,y,heights):
			minima.append([x,y])
	
cumSum = 0	
for xy in minima:
	cumSum += heights[xy[0]][xy[1]] + 1
print(minima)
print(cumSum)