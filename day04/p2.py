def readBingoNums(input):
    bingoNumsStr = input[0].split(',')
    bingoNums = []
    for numStr in bingoNumsStr:
        bingoNums.append(int(numStr))
    return bingoNums

def readBingoBoards(input):
    board = []
    boards = []
    for line in input:
        if line == '\n':
            continue
        else:
            row = []
            for num in line.strip().split(" "):
                if num.isdigit():
                    row.append(int(num))
                    if len(row) == 5:
                        break
            board.append(row)
            if len(board) == 5:
                #print(board)
                boards.append(board)
                board = []
    return boards

def isWinningBoard(xs, ys):
    if 5 in xs or 5 in ys:
        return True
    return False
            
def getWinningIndex(board, nums):
    xs = [0,0,0,0,0]
    ys = [0,0,0,0,0]
    for idx,bingoNum in enumerate(nums):
        found = False
        for y,row in enumerate(board):
            for x,num in enumerate(row):
                if num == bingoNum:
                    xs[x] += 1
                    ys[y] += 1
                    found = True
                    break
            if found:
                break
        if isWinningBoard(xs,ys):
            return idx
    #This board will never win
    return len(nums)
    
def getWinningIndices(boards, nums):
    wins = []
    for board in boards:
        wins.append(getWinningIndex(board, nums))
    return wins
        
def findWinningBoard(boards, bingoNums):
    wins = getWinningIndices(boards, bingoNums)
    max = 0
    maxIdx = -1
    for idx,winningNumOfCalls in enumerate(wins):
        if winningNumOfCalls > max:
            max = winningNumOfCalls
            maxIdx = idx
        print(winningNumOfCalls, idx, max, maxIdx)
    return (maxIdx, max)
    
def getScore(board, bingoNums, winningCallIdx):
    cumSum = 0
    for row in board:
        for num in row:
            cumSum += num
    for num in bingoNums[:winningCallIdx+1]:
        for row in board:
            if num in row:
                cumSum -= num
                break
    return cumSum * bingoNums[winningCallIdx]
    
    
input = open("input.txt").readlines()
bingoNums = readBingoNums(input)
boards = readBingoBoards(input[2:])

winningBoardIdx,winningCallIdx = findWinningBoard(boards, bingoNums)
score = getScore(boards[winningBoardIdx], bingoNums, winningCallIdx)

print(score)




'''
nums = set()
for num in bingoNums:
    if num in nums:
        print("duplicate")
        nums.add(num)
print("noduplicates")
'''