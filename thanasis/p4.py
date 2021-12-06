import sys

def updateBoard(board, num):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == num:
                board[i][j] = -1

def checkBoard(board):
    for row in board:
        if sum(row) == -len(row):
            return True
    
    for col in zip(*board):
        if sum(col) == -len(col):
            return True
    
    return False

def findSum(board):
    # return sum[board[i][j] for i in range(len(board)) for j in range(len(board[0])) if board[i][j] != -1]
    s = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != -1:
                s += board[i][j]
    return s

def parse_input():
    with open(sys.argv[1]) as file:
        boards = []
        for i, line in enumerate(file.readlines()):
            if i == 0:
                randomNumbers = [int(i) for i in line.split(',')]
                board = []
            else:
                if line == '\n':
                    if board != []:
                        boards.append(board)
                    board = []
                    continue
                else:
                    row = [int(i) for i in line.split(' ') if i != '']
                    board.append(row)
        boards.append(board)
        return randomNumbers, boards

def ex1(randomNumbers, boards):
    for num in randomNumbers:
        for i, board in enumerate(boards):
            updateBoard(board, num)
            if checkBoard(board):
                return num * findSum(board)

def ex2(randomNumbers, boards):
    checkedBoards = [i for i in range(len(boards))]
    for num in randomNumbers:
        for i, board in enumerate(boards):
            updateBoard(board, num)
            if checkBoard(board) and i in checkedBoards:
                checkedBoards.remove(i)
                if checkedBoards == []:
                    return num * findSum(board)

if __name__ == "__main__":
    randomNumbers, boards = parse_input()
    print(ex1(randomNumbers, boards))
    print(ex2(randomNumbers, boards))
