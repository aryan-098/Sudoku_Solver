import pygame
import time
import random

pygame.init()
pygame.font.init()

WIDTH,HEIGHT=540,540
GRID_SIZE=9
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# Display screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")


# Font 
font = pygame.font.Font(None, 40)


# Get random questions from file
def GetQuestion(filename):
    with open(filename, 'r') as file:
        content = file.read().strip()
    
    puzzles = content.split("\n---\n")  # Split puzzles using separator "---"
    random_puzzle = random.choice(puzzles)  # Pick a random puzzle
    
    # Only process valid rows (skip any separator lines)
    board = []
    for line in random_puzzle.split("\n"):
        # Skip any empty lines or separator lines
        if line.strip() and line != '---':
            board.append([int(num) for num in line.split()])
    
    return board



board=GetQuestion(r"D:\Python\Project\SudokuQuestions.txt")




def draw_board():
    screen.fill(WHITE)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            num = board[row][col]
            if num != 0:
                color = BLACK
                text = font.render(str(num), True, color)
                screen.blit(text, (col * CELL_SIZE + 20, row * CELL_SIZE + 15))

    # Draw grid lines
    for i in range(GRID_SIZE + 1):
        line_width = 3 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), line_width)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), line_width)

    pygame.display.update()



# Function to draw a number in a cell (with color for backtracking/placing)
def draw_cell(row, col, num, color):
    pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    if num != 0:
        text = font.render(str(num), True, color)
        screen.blit(text, (col * CELL_SIZE + 20, row * CELL_SIZE + 15))

    pygame.display.update()




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
                        draw_cell(row, col, num, BLUE)  # Show number being placed in blue
                        pygame.time.delay(1)  # Delay to create animation effect

                        if solve(board):  #recursion
                            return True
                    
                        #backtracking
                        board[row][col]=0 
                        draw_cell(row, col, 0, RED)  # Show backtracking in red
                        pygame.time.delay(1)  # Delay to create animation effect

                return False
    return True




def print_board(board):
    for row in board:
            print(" ".join(str(num) if num!=0 else '_' for num in row))




def main():
    draw_board()
    pygame.time.delay(500)  # Initial delay to show the start of the board
    start_time=time.time()
    print("Original Sudoku Board:")
    print_board(board)
    if solve(board):
        print("Solved Sudoku Board is: ")
        print_board(board)
        end_time=time.time()
        print(f"Time Taken: {round(end_time - start_time, 3)} seconds")  # Debugging
    else:
        print("Sudoku cannot be solved")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()



# Run the Sudoku solver with Pygame animation
if __name__ == "__main__":
    main()