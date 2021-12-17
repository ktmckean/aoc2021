
def getHeaderInfo(packet, binPos):
	strPos = int(binPos / 4)
	offset = binPos%4
	
	vnum = getBit(packet, binPos)
	vnum *=2
	vnum += getBit(packet, binPos+1)
	vnum *=2
	vnum += getBit(packet, binPos+2)
	binPos += 3

	tid = getBit(packet, binPos)
	tid *=2
	tid += getBit(packet, binPos+1)
	tid *=2
	tid += getBit(packet, binPos+2)
	binPos += 3
	
	#print("version num: ",vnum, 'tid: ',tid)
	return vnum,tid
	
def getBit(bigPacket, binPos):
	strPos = int(binPos / 4)
	offset = binPos%4
	hexDigit = int(bigPacket[strPos], 16)
	bit = getBitFromHexPos(hexDigit, offset)
	#print(binPos, bigPacket[strPos], hexDigit, bin(hexDigit), offset, bit)
	return bit


def getBitFromHexPos(hexDigit, offset):
	placeValue = 8
	
	for i in range(offset):
		hexDigit = hexDigit % placeValue
		placeValue = int(placeValue/2)
	
	if hexDigit >= placeValue:
		return 1
	return 0
	
def readFourDigits(packet, binPos):
	num = 0
	for i in range(4):
		num *= 2
		bit = getBit(packet,binPos)
		#print('adding a ',bit)
		num += bit
		binPos += 1
		
	return num

def getLengthOfLiteral(bigPacket,binPos):
	startPos = binPos
	#binPos += 6		# header length; all literals are at least this long
	#print('reading literal from pos',startPos,'...')
	more = True
	num = 0
	while more:
		bit = getBit(bigPacket, binPos)
		binPos += 1
		num += readFourDigits(bigPacket,binPos)
		binPos += 4
		
		if bit == 0:
			more = False
		else:
			num *= 16
			#print('num after shifting: ',num)
			print('continuing...')
	
	print('read literal of value ',num)
	
	return binPos - startPos
	
def get15bitLength(packet,binPos):
	l = 0
	for i in range(15):
		l *= 2
		l += getBit(packet,binPos)
		binPos += 1
	return l

def get11bitNumber(packet,binPos):
	n = 0
	for i in range(11):
		n *= 2
		n += getBit(packet,binPos)
		binPos += 1
	return n

def readOperatorPacket(packet,binPos):
	lengthTypeId = getBit(packet, binPos)
	binPos += 1

	pLength = 1
	vsum = 0
	if lengthTypeId == 0:
		#the next 15 bits represent a number indicating the total number of bits in my sub-packets
		subLength = get15bitLength(packet,binPos)
		binPos += 15
		pLength += 15
		vsum = readPacketBySize(packet,binPos,subLength)
		pLength += subLength		
		
	elif lengthTypeId == 1:
		#the next 11 bits represent a number indicating the immediate number of sub-packets contained by me
		num = get11bitNumber(packet,binPos)
		binPos += 11
		pLength += 11
		vsum,subLength = readPacketByNumber(packet,binPos,num)
		pLength += subLength

	else:
		print('something has gone horribly wrong.  This isn\'t binary anymore')
	
	print('sum',vsum)
	return vsum,pLength

def readPacketBySize(packet,binPos,length):
	startPos = binPos
	versionSum = 0
	
	while startPos + length > binPos:
		vnum,tid = getHeaderInfo(packet,binPos)
		versionSum += vnum
		print("reading",(binPos-startPos),"of",length,"bits by size. vnum = ", vnum,'tid=',tid)	
		binPos += 6
		if tid == 4:
			# we have a literal
			binPos += getLengthOfLiteral(packet, binPos)
		else:
			vsum,subLength = readOperatorPacket(packet,binPos)
			binPos += subLength
			versionSum += vsum
	
	print('sum:',versionSum)
	return versionSum

def readPacketByNumber(packet,binPos,number):
	startPos = binPos
	
	versionSum = 0
	numPackets = 0
	while numPackets < number:
		vnum,tid = getHeaderInfo(packet,binPos)
		binPos += 6
		versionSum += vnum
		print("reading",numPackets+1,"of",number,"packets by num. vnum =", vnum, 'tid =',tid)

		if tid == 4:
			# we have a literal
			binPos += getLengthOfLiteral(packet, binPos)
			numPackets += 1
		else:
			# we have an operator packet
			vsum,subLength = readOperatorPacket(packet,binPos)
			binPos += subLength
			numPackets += 1
			versionSum += vsum

	print('sum =',versionSum)	
	return versionSum, (binPos - startPos)


def readWholePacket(packet):
	notAtEnd = True
	binPos = 0
	versionSum = 0
	while binPos < len(packet):
		vnum, tid = getHeaderInfo(packet, binPos)
		print('reading top-level packet. vnum =',vnum,'tid =',tid)
		binPos += 6
		versionSum += vnum
		
		if tid == 4:
			binPos += getLengthOfLiteral(packet, binPos)
		else:
			vsum,length = readOperatorPacket(packet,binPos)
			binPos += length
			versionSum += vsum
		print('CumSum',versionSum)
	return versionSum		



fullString = open("input.txt").readline().strip()
print(readWholePacket(fullString))


'''
s = int('b',16)
print(s)


hexStr = '1111'
print(bin(int(hexStr,16)))

s = 3
print(s>>1)

s = 1
print(s<<1)
'''