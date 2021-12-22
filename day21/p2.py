import copy

class Player:
	def __init__(self,pos,score):
		self.pos = pos
		self.score = score

def readStartingPositions():
	file = open('input.txt')
	l1 = file.readline().strip()
	l2 = file.readline().strip()
	
	return int(l1[-1]),int(l2[-1])
	
def playPracticeGame(p1start, p2start):
	p1 = Player(p1start-1,0)
	p2 = Player(p2start-1,0)
	die = 0
	numRolls = 0
	turn = 1
	while True:
		move = 0
		for i in range (3):
			move += (die+1)
			die += 1
			die = die % 100
			numRolls += 1
		
		if turn == 1:
			p1.pos = (p1.pos + move) % 10
			p1.score = p1.score + p1.pos + 1
			turn = 2
			if p1.score >= 1000:
				print('p1 wins!  score: ',p1.score,p2.score, numRolls)
				print(p2.score * numRolls)
				exit()
			#else:
			#	print('p1 moved to space ',p1.pos+1, p1.score)
		elif turn == 2:
			#print(p2.pos)
			p2.pos = (p2.pos + move) % 10
			#print(p2.pos)
			p2.score = p2.score + p2.pos + 1
			turn = 1
			if p2.score >= 1000:
				print('p2 wins!  score: ',p1.score,p2.score, numRolls)
				print(p1.score * numRolls)
				exit()
			#else:
			#	print('p2 moved',move,'spaces to space ',p2.pos+1, p2.score)
		else:
			print('turn is neither one nor two!')

def totalNumGames(places):
	sumGames = 0
	for scoreCounts in places.values():
		for score,numGames in scoreCounts.items():
			sumGames += numGames
	return sumGames

def takeTurn(places, dieRolls):
	newPlaces = copy.deepcopy(places)
	allDone = True
	wins = 0
	#print(places)
	
	for oldPlace,scoreCounts in places.items():
		for oldScore,numGames in scoreCounts.items():
			if numGames == 0:
				#print('skipping ',oldPlace, oldScore)
				continue
			else:
				allDone = False
				#print(oldPlace, oldScore, numGames)

			for rollVal,rollCount in dieRolls.items():
				newPlace = (oldPlace + rollVal) % 10
				newScore = oldScore + newPlace + 1
				
				if newScore >= 21:
					wins += numGames*rollCount
					#numWinningRolls += 1
					#print('adding',numGames,'*',rollCount,'=',numGames*rollCount,'wins from oldScore',oldScore)
					#newPlaces[oldPlace][oldScore] -= numGames
				else:
					if newScore not in newPlaces[newPlace].keys():
						newPlaces[newPlace][newScore] = 0
					newPlaces[newPlace][newScore] += numGames * rollCount
					
					#print(oldPlace,rollVal, newPlaces)
			newPlaces[oldPlace][oldScore] -= numGames

	#assert(totalNumGames(newPlaces) == totalNumGames(otherPlayer))
		#if not allDone: print(oldPlace,newPlaces)
	return newPlaces, wins, allDone

def updateOtherPlayer(places,multiple):
	newPlaces = copy.deepcopy(places)
	#print(increase, losses,newPlaces)
	for place,scoreCounts in places.items():
		for score,count in scoreCounts.items():
			if count == 0:
				continue
			else:
				#print(place, score,count)
				newPlaces[place][score] *= multiple
				if not newPlaces[place][score].is_integer:
					print(newPlaces[place][score])
					assert(false)
				else:
					newPlaces[place][score] = int(newPlaces[place][score])
				#newPlaces[place][score] -= losses
				assert(newPlaces[place][score] >= 0)
	print(multiple, newPlaces)
	return newPlaces

def buildDieRolls():
	dieKeys = [3,4,5,6,7,8,9]
	dieVals = [1,3,6,7,6,3,1]
	dieRolls = dict(zip(dieKeys,dieVals))
	return dieRolls

def buildPlaces():
	placeKeys = [0,1,2,3,4,5,6,7,8,9]
	placeVals = [{},{},{},{},{},{},{},{},{},{}]
	places = dict(zip(placeKeys,placeVals))
	return places

def playRealGames(p1start,p2start):
	# plan is to keep increasing the number of die rolls until all possible outcomes result in finished games.
	# For each string of length N, we will add the number of wins to the winning player's count.
	# NOTE: There is no reason to keep track of the player's rolls separately (only if we can keep track of who has won already)
	dieRolls = buildDieRolls()
	places1 = buildPlaces()
	places1[p1start-1] = dict(zip([0],[1]))
	places2 = buildPlaces()
	places2[p2start-1] = dict(zip([0],[1]))
	
	
	wins1 = 0
	wins2 = 0
	allDone = False
	whoseTurn = 1
	numTurns = 1
	while not allDone:
	#for i in range(5):
		if whoseTurn == 1:
			oldNumGames = totalNumGames(places1)
			newPlaces, wins, allDone = takeTurn(places1,dieRolls)
			wins1 += wins
			if allDone:
				break
			newNumGames = totalNumGames(newPlaces)

			places1 = newPlaces.copy()
			increase = newNumGames / oldNumGames
			places2 = updateOtherPlayer(places2,increase)
			assert(totalNumGames(places1) == totalNumGames(places2))
			
			whoseTurn = 2
		else:
			oldNumGames = totalNumGames(places2)
			newPlaces, wins, allDone = takeTurn(places2,dieRolls)
			wins2 += wins
			if allDone:
				break
			newNumGames = totalNumGames(newPlaces)
			
			places2 = newPlaces.copy()
			increase = newNumGames / oldNumGames
			places1 = updateOtherPlayer(places1,increase)			
			assert(totalNumGames(places1) == totalNumGames(places2))

			whoseTurn = 1
		
		numTurns += 1
		#print(sumGames(newPlaces)
	
		'''	
		newPlaces = places.copy()
		for oldPlace,scoreCounts in places.items():
			for oldScore,numGames in scoreCounts.items():
				if numGames == 0:
					continue
				#else:
				#	allDone = False

				for rollVal,rollCount in dieRolls.items():
					newPlace = (oldPlace + rollVal) % 10
					newScore = oldScore + newPlace + 1
					
					if newScore >= 21:
						wins += numGames * rollCount
						newPlaces[oldPlace][oldScore] -= numGames
					else:
						if newScore not in newPlaces[newPlace].keys():
							newPlaces[newPlace][newScore] = 0
							
						newPlaces[newPlace][newScore] += numGames * rollCount
						#print(oldPlace,rollVal, newPlaces)
				newPlaces[oldPlace][oldScore] -= numGames

			#print(oldPlace,newPlaces)
		'''
		#print('took turn')
		#print(newPlaces)
	return max(wins1, wins2)

	
	
	
	
			
p1,p2 = readStartingPositions()
#print(p1,p2)
#playPracticeGame(p1,p2)

winner = playRealGames(p1,p2)
print(winner)

'''
	# times	sum
111			3
112	3		4
113	3		5
122	3		5
123	6		6
133	3		7
222			6
223	3		7
233	3		8
333			9

#sum	#times
3		1
4		3
5		6
6		7
7		6
8		3
9		1
'''








		
			