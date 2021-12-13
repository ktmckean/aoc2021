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

def generatePathRecursive(path, rooms, completed):
	path = path.copy()
	if path[-1] == 'end':
		completed.append(path)
		return completed
		
	path.append('')
	for exit in rooms[path[-2]]:
		if exit.islower() and exit in path:
			#print("skipping "+exit)
			continue
		else:
			path[-1] = exit
			#print(path)#, ' : diving into ', path[-1])
			completed = generatePathRecursive(path,rooms,completed)
	return completed

def findAllPaths(rooms):
	path = ['start']
	completed = []
	visited = set()
	return generatePathRecursive(path,rooms,completed)

rooms = readInRooms()
#print(str('A').isupper())
print(rooms)
a = findAllPaths(rooms)
print(len(a))
