def readInput():
	cmds = []
	for line in open('input.txt'):
		cmd = []
		line = line.strip()
		if line.split(' ')[0] == 'on':
			cmd.append(1)
		elif line.split(' ')[0] == 'off':
			cmd.append(0)
		else:
			print('neither on nor off')
			exit()
		
		ranges = line.split(' ')[1]
		dims = ranges.split(',')
		for r in dims:
			nums = r.split('=')[1].split('..')
			cmd.append([int(nums[0]),int(nums[1])])
		cmds.append(cmd)
	return cmds
	
def intersectFiftyCube(cmd):
	for dim in cmd[1:]:
		l1 = dim[0] <= -50
		l2 = dim[1] <= -50
		g1 = dim[0] >= 50
		g2 = dim[1] >= 50
		if (l1 and l2) or (g1 and g2):
			return False
	return True
	
def findIntersection(box1,box2):
	overlapBox = []
	for i,dim in enumerate(box1):
		l1 = dim[0] <= box2[i][0]
		l2 = dim[1] <= box2[i][0]
		g1 = dim[0] >= box2[i][1]
		g2 = dim[1] >= box2[i][1]
		if (l1 and l2) or (g1 and g2):
			return []
		else:
			pt = [max(dim[0],box2[i][0]), min(dim[1],box2[i][1])]
			overlapBox.append(pt)
	return overlapBox
	
def boxSize(box):
	size = 1
	for dim in box:
		size *= dim[1]-dim[0]
	return size
	
def getOnBoxes(cmds):
	boxes = []
	for c in cmds:
		if c[0] == 1:
			boxes.append(cmd[1:])
	return boxes
	
# overlap possible and likely
def getAllIntersections(box1,boxes):
	intersects = [findIntersection(box1, boxes[0])]
	for b in boxes[1:]:
		i = findIntersection(box1,b)
		if i = []:
			continue
		else:
			intersects.append(i)
	return intersects
	
def aContainsB(a,b):
	if a[0][0] > b[0][0] or a[0][1] < b[0][[1]:
		return False
	if a[1][0] > b[1][0] or a[1][1] < b[1][[1]:
		return False
	if a[2][0] > b[2][0] or a[2][1] < b[2][[1]:
		return False
	return True
	
	
def reduceOverlap(b1,b2)
	overlap = findIntersection(b1,b2)
	if overlap == []:
		return [b1,b2]
	elif b1 == b2:
		return [b1]
	
	#three options:
	#hole: one contains the other
	#pierce: one contains the other in 
		
		
	for i,dim in enumerate(b1):
		extendsLower = dim[0] < overlap[i][0]
		extendsHigher = dim[1] > overlap[i][1]
		
		lowerb1 = []
		if extendsLower:
			lowerb1.append([dim[0],overlap[i][0]
		
		smallerb1
		
		
	#condition of overlap
	lower = []
	higher = []
	if b1[i][0] < b2[i][0]:
		lower = b1
		higher = b2
	else:
		lower = b2
		higher = b1
	
	# This must be true if there's an overlap
	assert(lower[0][1] >= higher[0][0])
	retList = []
	if lower[0][1] <= higher[0][1]:
		#this is a one segment problem
		xes = 
		ys = [lower[1][0],lower[1][1]]
		zs = [lower[2][0],lower[2][1]]
		
		
		retList.append([[xes],[ys],[zs]]
		
		
	elif lower[i][1] > higher[i][1]:
		#this is a two segment problem
	
	
	
		

def getUniqueIntersections(b0,boxes):
	allIntersects = getAllIntersections(b0,boxes)
	
	intersectingPairs = []
	for i,b1 in enumerate(boxes):
		for j,b2 in enumerate(boxes):
			if i != j:
				b1b2 = findIntersection(b1,b2)
				
				
				
				intersectingPairs.append([i,j])
	if len(intersectingPairs) == 0:
		return allIntersects
	else:
		

'''
def reduceDuplicateIntersections(intersects):
	reduced = []
	for i in intersects:
		isUnique = True
		for j in intersects:
			ij = findIntersection(i,j)
			if ij != []:
				isUnique = False
				#do some stuff with the zone ij
		
		if isUnique:
'''	

	
cmds = readInput()

onCount = 0
for i,cmd in enumerate(cmds):
	if not intersectFiftyCube(cmd):
		continue
	
	if cmd[0] == 1:
		size = boxSize(cmd[1:])
		onCount += boxSize(cmd[1:])
		priorBoxes = getOnBoxes(cmds[:i])
		#for every unique overlap with an on region:
		# 	subtract overlap volume, less volume where overlap was turned off
		#for every overlap with an off region
		#	
		intersects = getAllIntersections(cmd[1:],

print(onCount)

a = [1,2,3,4,5]
print(a[0:2,3:])
	
	#if on:
	#	numOn += size of new box - sum of sizes of overlaps with all existing boxes (reduced so no overlap is included more than once)
	#if off
	#	same but -=
	
	

