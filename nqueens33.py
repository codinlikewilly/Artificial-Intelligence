import random
import copy

success = 0
block = 1
queen = 2
trials = 0
x=0
s=0


size = input("How big is the board?: ")
size = int(size)

#make board
def get_board(size):
    board = [0]*size
    for ix in range(size):
        board[ix] = [0]*size
    return board

def print_solutions(solutions, size):
    for sol in solutions:
        for row in sol:
            print(row)
        print()
            
def is_safe(board, row, col, size):
    """Check if it's safe to place a queen at board[x][y]"""

    #check row on left side
    for iy in range(col):
        if board[row][iy] == 1:
            return False
    
    ix, iy = row, col
    while ix >= 0 and iy >= 0:
        if board[ix][iy] == 1:
            return False
        ix-=1
        iy-=1
    
    jx, jy = row,col
    while jx < size and jy >= 0:
        if board[jx][jy] == 1:
            return False
        jx+=1
        jy-=1
    
    return True

def solve(board, col, size):
    """Use backtracking to find all solutions"""
    #base case
    if col >= size:
        return
    
    for i in range(size):
        if is_safe(board, i, col, size):
            board[i][col] = 1
            if col == size-1:
                add_solution(board)
                board[i][col] = 0
                return
            solve(board, col+1, size)
            #backtrack
            board[i][col] = 0

def add_solution(board):
    """Saves the board state to the global variable 'solutions'"""
    global solutions
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)


board = get_board(size)

solutions = []

solve(board, 0, size)

print_solutions(solutions, size)

print("Total solutions = {}".format(len(solutions)))


#NQ = [random.randint(0,n-1) for x in range(n)]
#board = [[0 for x in range(n)]for y in range(n)]
#board = [[]]

#board = get_board(n)
#solutions = []
#solve(board,0,n)
#print(board)
    



    



#print (NQ[2])

#print(*NQ, sep='\n')

#print(*board, sep='\n')





