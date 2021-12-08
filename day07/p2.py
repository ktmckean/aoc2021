input = open("input.txt").readline()
crabs = []
for pos in input.split(','):
	crabs.append(int(pos))

min = min(crabs)
max = max(crabs)
if min != 0:
	print("min is not zero! offset")

movementCosts = [0]
for i in range(1, max+1):
	movementCosts.append(i + movementCosts[i-1])
print(movementCosts)

fuelCosts = {}
for pos in range(max - min):
	fuelCumSum = 0
	for crab in crabs:
		fuelCumSum += movementCosts[abs(crab - pos)]
	fuelCosts[pos] = fuelCumSum

#print(fuelCosts)
minCost = max * max * max
for cost in fuelCosts.values():
	if cost < minCost:
		minCost = cost

print(minCost)