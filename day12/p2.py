def readInRooms():
	rooms = {}
	for line in open("input.txt"):
		line = line.strip()
		edge = line.split('-')
		
		startRoom = edge[0]
		endRoom = edge[1]
		if startRoom in rooms.keys():
			rooms[startRoom].add(endRoom)
		else:
			rooms[startRoom] = {endRoom}
		
		startRoom = edge[1]
		endRoom = edge[0]
		if startRoom in rooms.keys():
			rooms[startRoom].add(endRoom)
		else:
			rooms[startRoom] = {endRoom}
	return rooms

def generatePathRecursive(path, rooms, completed, doubledBack):
	path = path.copy()
	if path[-1] == 'end':
		completed.append(path)
		return completed
		
	path.append('')
	for exit in rooms[path[-2]]:
		if exit.islower() and exit in path:
			if doubledBack or exit=='start':
				continue
			else:
				path[-1] = exit
				doubledBack = 1
				completed = generatePathRecursive(path,rooms,completed,doubledBack)
				doubledBack = 0
		else:
			path[-1] = exit
			completed = generatePathRecursive(path,rooms,completed,doubledBack)
	return completed

def findAllPaths(rooms):
	path = ['start']
	completed = []
	visited = set()
	return generatePathRecursive(path,rooms,completed,0)

rooms = readInRooms()
a = findAllPaths(rooms)

print(len(a))
