input = open("input.txt").readline()
crabs = []
for pos in input.split(','):
	crabs.append(int(pos))

min = min(crabs)
max = max(crabs)
if min != 0:
	print("min is not zero! offset")

fuelCosts = {}
for pos in range(max - min):
	fuelCumSum = 0
	for crab in crabs:
		fuelCumSum += abs(crab - pos)
	fuelCosts[pos] = fuelCumSum

#print(fuelCosts)
minCost = max * max * max
print(minCost)
for cost in fuelCosts.values():
	if cost < minCost:
		minCost = cost

print(minCost)