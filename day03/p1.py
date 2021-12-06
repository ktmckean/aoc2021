
counts = [[0 for i in range(2)] for j in range(12)]

for line in open("input.txt"):
    idx = 0
    for char in line.strip():
        if char == '0':
            counts[idx][0] += 1
        elif char == '1':
            counts[idx][1] += 1
        else:
            print("Error! non-digit character detected")
            print("it was %s", char)
            exit()
        idx += 1
    
print(counts)

decimalGamma = 0
decimalEpsilon = 0

for digit in counts:
    decimalGamma *= 2
    decimalEpsilon *= 2
    if digit[0] > digit[1]:
        decimalEpsilon += 1
    elif digit[0] < digit[1]:
        decimalGamma += 1
    else:
        print("error! they are equal!")
        print(digit)
        exit()
    print([decimalEpsilon, decimalGamma])
        
print(decimalGamma)
print(decimalEpsilon)
print(decimalGamma * decimalEpsilon)
