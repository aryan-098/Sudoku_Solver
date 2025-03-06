import time
def isvalid(board,row,col,num): #checking the rules of Sudoku
    for i in range(9):
        if board[row][i]==num or board[i][col]==num:
            return False
        
    #3X3 box
    start_row,start_col=(row//3)*3,(col//3)*3
    for row in range(start_row,start_row+3):
        for col in range(start_col,start_col+3):
            if board[row][col]==num:
                return False
    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col]==0:
                for num in range(1,10):
                    if isvalid(board,row,col,num):
                        board[row][col]=num

                        if solve(board):  #recursion
                            return True
                    
                        #backtracking
                        board[row][col]=0 

                return False
    return True


def print_board(board):
    for row in board:
            print(" ".join(str(num) if num!=0 else '_' for num in row))

sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Original Sudoku Board:")
print_board(sudoku_board)
start_time=time.time()
if solve(sudoku_board):
    print("Solved Sudoku Board is: ")
    print_board(sudoku_board)
    end_time=time.time()
    print(end_time-start_time)
else:
    print("Sudoku cannot be solved")