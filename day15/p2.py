import copy

def buildGraph():
	graph = []
	for line in open("input.txt"):
		line = line.strip()
		row = []
		for char in line:
			row.append(int(char))
		graph.append(row)
	
	#extend each row
	for y,row in enumerate(graph):
		origRow = copy.deepcopy(row)
		bonus = 0
		#print(row)
		for i in range(4):
			bonus += 1
			for num in origRow:
				newNum = num + bonus
				if newNum > 9:
					newNum -= 9
				graph[y].append(newNum)
		#print(graph[y])
		
	origGraph = copy.deepcopy(graph)
	bonus = 0
	for i in range(4):
		bonus += 1
		#print(len(graph), bonus)
		for row in origGraph:
			newRow = []
			for num in row:
				newNum = num + bonus
				if newNum > 9:
					newNum -= 9
				#print(num, newNum)
				newRow.append(newNum)
			graph.append(newRow)
	
	return graph


def getRiskToPt(x,y, risks, graph):
	risk = 0
	if x == 0 and y  == 0:
		return risk
	elif y==0:
		risk = risks[y][x-1] + graph[y][x]
	elif x==0:
		risk = risks[y-1][x] + graph[y][x]
	else:
		risky = risks[y-1][x] + graph[y][x]
		riskx = risks[y][x-1] + graph[y][x]
		risk = min(risky,riskx)
	return risk

def updateNeighbors(x,y, risks, graph):
	if x == 0 and y  == 0:
		return risks
	
	if risks[y][x] == 0:
		print("error!  We are updating something that hasn't been filled in yet")
		exit()
	
	if y != 0 and risks[y-1][x] > risks[y][x] + graph[y-1][x]:
		risks[y-1][x] = risks[y][x] + graph[y-1][x]
		#print("updating neighbor at: " + str(x) +' , ' +str(y-1))
		risks = updateNeighbors(x,y-1,risks,graph)
		
	if x != 0 and risks[y][x-1] > risks[y][x] + graph[y][x-1]:
		risks[y][x-1] = risks[y][x] + graph[y][x-1]
		#print("updating neighbor at: " + str(x-1) +' , ' +str(y))
		risks = updateNeighbors(x-1,y,risks,graph)
	
	if y+1 < len(graph) and risks[y+1][x] != 0:
		if risks[y+1][x] > risks[y][x] + graph[y+1][x]:
			risks[y+1][x] = risks[y][x] + graph[y+1][x]
			#print("updating neighbor at: " + str(x) +' , ' +str(y+1))
			risks = updateNeighbors(x,y+1,risks,graph)	

	#print(x+1, len(graph[0]), len(risks[0]))
	if x+1 < len(graph[0]) and risks[y][x+1] != 0:
		if risks[y][x+1] > risks[y][x] + graph[y][x+1]:
			risks[y][x+1] = risks[y][x] + graph[y][x+1]
			#print("updating neighbor at: " + str(x) +' , ' +str(y+1))
			risks = updateNeighbors(x+1,y,risks,graph)		
	
	
	return risks
	
	
def evaluateRisks(graph):
	risks = [[0 for i in range(len(graph[0]))] for j in range(len(graph))]
	#risks = [[0 for i in range(10)] for j in range(10)]
	
	for y,row in enumerate(risks):
		for x,col in enumerate(row):
			risks[y][x] = getRiskToPt(x,y,risks,graph)
			risks = updateNeighbors(x,y,risks,graph)
	
	return risks
			
			
graph = buildGraph()
outFile = open('output.txt', 'a')
for row in graph:
	for num in row:
		outFile.write(str(num))
	outFile.write('\n')

#print(graph)
risks = evaluateRisks(graph)


#print(risks)
print(risks[-1][-1])