from copy import deepcopy

def buildGraph():
	graph = []
	for line in open("input.txt"):
		line = line.strip()
		row = []
		for char in line:
			row.append(int(char))
		graph.append(row)
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
risks = evaluateRisks(graph)


print(risks)