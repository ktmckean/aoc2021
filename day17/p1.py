
def getMaxHeight(vy):
	return int((vy * (vy+1))/2)
	'''height = 0
	for i in range(vy+1):
		height += i
	return height'''
	
def getMaxDistance(vx):
	return int((vx * (vx+1))/2)
	'''xf = 0
	for i in range(vx+1):
		xf += i
	return xf
	'''
	
def getyAfterSteps(vy,steps):
	vy = -1*vy -1
	for i in range(steps):
		
	

def getVxRange(xmin,xmax):
	vxmin = 0
	vxmax = 0
	while True:
		if getMaxDistance(vxmin) < xmin:
			vxmin += 1
			vxmax += 1
			continue
		if getMaxDistance(vxmax) < xmax:
			vxmax += 1
			continue
		break
	return vxmin,vxmax
	
def getVyRange(ymin,ymax,maxSteps):
	vxmax = 0
	while True:
		if getMax
		
	
def vxSteps(xmin,xmax,vx):
	x = 0
	steps = 0
	while vx > 0 and x <= xmax:
		if x >= xmin and x <= xmax:
			return steps
		x += vx
		vx -= 1
		steps += 1
	return -1
	
def vySteps(ymin,ymax,vy,maxSteps):
	y = 0
	steps = 0
	peaked = False
	while not peaked and y >= ymin and steps<maxSteps:
		if y >= ymin and y <= ymax:
			return steps
		y += vy
		vy -= 1
		steps += 1
		if vy < 1: peaked = True
	return -1

def getValidXes(xmin,xmax):
	vx,vxmax = getVxRange(xmin,xmax)
	valid = {}
	
	while vx < vxmax:
		steps = vxSteps(xmin,xmax,vx)
		if steps != -1:
			valid[vx] = steps
		vx += 1
	return valid

def getValidYs(ymin,ymax,maxSteps):
	vy,vymax = getVyRange(ymin,ymax)
	valid = []
	
	while vy < vymax:
		steps = vySteps(ymin,ymax,vy)
		if steps != -1:
			valid[vy] = steps
		vy += 1
	return valid

def getValidCombos(xmin,xmax,ymin,ymax):
	xes = getValidXes(xmin,xmax)
	ys = getValidYs(ymin,ymax)
	ySteps = {}
	for y,steps in ys:
		if ySteps[steps] == None:
			ySteps[steps] = [y]
		else:
			ysteps[steps].append(y)
	
	combos = []
	for x,steps in xes:
		for y in ySteps[steps]:
			combos.append(x,y)
			
	return combos

def getHighestY(combos):
	yMax = 0
	for xy in combos:
		if xy[1] > yMax:
			yMax = xy[1]
	return getMaxHeight(yMax)


line = open('input.txt').readline()
xmin = int(line[15:18])
xmax = int(line[20:23])
ymin = int(line[27:31])
ymax = int(line[33:36])

combos = getValidCombos(xmin,xmax,ymin,ymax)
print(getHighestY(combos))