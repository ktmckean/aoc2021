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

def roomHasExit(rooms, room, visited):
	for exit in rooms[room]:
		if exit not in visited:
			return True
	return False

def getNextRoom(rooms, path, visited):
	for exit in rooms[room]:
		if exit not in visited:
			return exit

def generatePathRecursive(path, rooms, completed, double):
	path = path.copy()
	if path[-1] == 'end':
		completed.append(path)
		return completed
		
	path.append('')
	for exit in rooms[path[-2]]:
		if exit.islower() and exit in path:
			#print("skipping "+exit)
			if double or exit=='start':
				continue
			else:
				double = exit
				path[-1] = exit
				completed = generatePathRecursive(path,rooms,completed,double)
				double = 0
		else:
			path[-1] = exit
			completed = generatePathRecursive(path,rooms,completed,double)
	return completed

def findAllPaths(rooms):
	path = ['start']
	completed = []
	visited = set()
	return generatePathRecursive(path,rooms,completed,0)

rooms = readInRooms()
a = findAllPaths(rooms)

print(len(a))
