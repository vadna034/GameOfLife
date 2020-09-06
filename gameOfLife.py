from copy import deepcopy

ROWS = 10
COLS = 10
DAY = 0

global board
row = [1] * COLS
board = []
for i in range(ROWS):
    board.append(deepcopy(row))

def onBoard(i, j):
    return i >= 0 and i < ROWS and j >= 0 and j < COLS

def update():
    global board
    prevDay = deepcopy(board)
    for i in range(ROWS):
        for j in range(COLS):
            count = 0
            count += (onBoard(i-1, j-1) and prevDay[i-1][j-1])    # i-1, j-1
            count += (onBoard(i-1, j) and prevDay[i-1][j-1])      # i-1, j
            count += (onBoard(i-1, j+1) and prevDay[i-1][j+1])    # i-1, j+1
            count += (onBoard(i, j+1) and prevDay[i][j+1])   # i, j+1
            count += (onBoard(i+1, j+1) and prevDay[i+1][j+1])   # i+1, j+1
            count += (onBoard(i+1, j) and prevDay[i+1][j])   # i+1, j
            count += (onBoard(i+1,j-1) and prevDay[i+1][j-1])   # i+1, j-1
            count += (onBoard(i, j-1) and prevDay[i][j-1])   # i, j-1

            if board[i][j]:
                if(i == 0 and j == 0):
                    print (int(count == 2 or count == 3))
                board[i][j] = int(count == 2 or count == 3)
            else:
                board[i][j] = int(count == 3)

            

        
def printBoard():
    global DAY
    DAY += 1
    print('Board on day number', DAY)
    for row in board:
        print(row)
    print('-\n-\n-\n')

while (DAY < 1):
    update()
    printBoard()