class Player:
	def __init__(self,pos,score):
		self.pos = pos
		self.score = score

def readStartingPositions():
	file = open('input.txt')
	l1 = file.readline().strip()
	l2 = file.readline().strip()
	
	return int(l1[-1]),int(l2[-1])
	
def takeTurn(player):
	ptemp = player.copy()
	ptemp.pos
	
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
			else:
				print('p1 moved to space ',p1.pos+1, p1.score)
		elif turn == 2:
			print(p2.pos)
			p2.pos = (p2.pos + move) % 10
			print(p2.pos)
			p2.score = p2.score + p2.pos + 1
			turn = 1
			if p2.score >= 1000:
				print('p2 wins!  score: ',p1.score,p2.score, numRolls)
				print(p1.score * numRolls)
				exit()
			else:
				print('p2 moved',move,'spaces to space ',p2.pos+1, p2.score)
		else:
			print('turn is neither one nor two!')

			
			
p1,p2 = readStartingPositions()
print(p1,p2)
playPracticeGame(p1,p2)

		
		
			