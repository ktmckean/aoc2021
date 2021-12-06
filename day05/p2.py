class Coord:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __str__(self):
		return "["+x+","++"]"

def readInput():
	lines = []
	for line in open("input.txt"):
		numStr = line.split(" -> ")
		nums = []
		for point in numStr:
			xy = point.split(',')
			nums.append(Coord(int(xy[0]), int(xy[1])))
		lines.append(nums)
	return lines
	
def getSeafloorSize(coordPairs):
	x = 0
	y = 0
	for pair in coordPairs:
		for coord in pair:
			x = max(coord.x,x)
			y = max(coord.y,y)
	return x+1,y+1


lines = readInput()
xymax = getSeafloorSize(lines)
seafloor = [ [0 for j in range(xymax[1])] for i in range(xymax[0])]
print(xymax)

a = 10
b = 5
l = abs(b-a)
print(l)
print(b + l)
#lines = [[Coord(0,0), Coord(5,5)], [Coord(2,2),Coord(2,3)]]

for line in lines:
	if line[0].x == line[1].x:
		length = abs(line[1].y - line[0].y)
		startY = min(line[0].y, line[1].y)
		for i in range(length + 1):
			seafloor[line[0].x][startY + i] += 1
	elif line[0].y == line[1].y:
		length = abs(line[1].x - line[0].x)
		startX = min(line[0].x, line[1].x)
		#print(startX, length, startX + length)
		for i in range(length + 1):
			seafloor[startX + i][line[0].y] += 1
	else:
		length = abs(line[1].x - line[0].x)
		start = line[0]
		xFactor = 5000
		yFactor = 5000
		
		start = line[0]
		if line[0].x < line[1].x:
			xFactor = 1
		else:
			xFactor = -1
		if line[0].y < line[1].y:
			yFactor = 1
		else:
			yFactor = -1

		print(start.x, start.y)
		print(xFactor)
		print(yFactor)
		for i in range(length + 1):
			#print(start.x + i*xFactor, start.y + i*yFactor)
			seafloor[start.x + i*xFactor][start.y + i*yFactor] += 1

numOverlaps = 0
for row in seafloor:
	for num in row:
		if num > 1:
			numOverlaps += 1

print(numOverlaps)