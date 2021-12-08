signals = []
outputs = []

for line in open("input.txt"):
	line = line.strip()
	print(line)
	patternStr,outputStr = line.split(" | ")
	signals.append(patternStr.split(" "))
	outputs.append(outputStr.split(" "))
	
outputLens = []
	
for output in outputs:
	lengths = []
	for signal in output:
		lengths.append(len(signal))
	outputLens.append(lengths)

print(outputs[0])
print(outputLens[0])
#print(outputLens)
count = 0
for output in outputLens:
	for num in output:
		if num == 2 or num == 3 or num == 4 or num == 7:
			count += 1
	print(output, count)
			
print(count)