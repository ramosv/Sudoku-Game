import checking
import random
import board_utils

"""
Backtracking algorthims will be the backbone of this implementation
We will be using backtracking to iterate through potential ways to solve the
board. If we ever encounter a move which leads to a dead end, we can backtrack
This process will continue to explore diffrent paths and number combinations
to make sure that the puzzle remains solvable.

"""


def valid_Move(sudoku, row,column,num):
    ##Place the number on the board temporarily

    save = sudoku[row][column]
    board_utils.add_number(sudoku,row,column,num)

    #Check if current movement is valud
    valid = (
        checking.row_correct(sudoku,row) and checking.column_correct(sudoku,column) and checking.block_correct(sudoku,3*(row // 3), 3*(column // 3))
    )

    # Restore the original number 
    board_utils.add_number(sudoku,row,column,save)

    return valid

def fill_board(sudoku):
    for i in range(9):
        for j in range(9):
            #Find an empty cell
            if sudoku[i][j] == 0:
                nums = list(range(1,10))
                #Randomize numbers in our list
                random.shuffle(nums)
                for num in nums:
                    if valid_Move(sudoku,i,j,num):
                        #If the number is valid, place it on the board
                        #print(f"Trying number {num} at position {i},{j}") 
                        sudoku[i][j] = num

                        #Depth-first search recursive call: Try to fill in the board completely
                        if fill_board(sudoku):
                            return True
                        #print(f"Backtracking from {i},{j}")  

                        ## Backtrack if no progress is made
                        sudoku[i][j] = 0

                #print(f"Failed to fill position {i},{j}, backtracking...") 
                ##Current board is not valid/solvable remove the number we just placed and return to the previous level of recursion to try a new number
                return False
            
    ## Board had succefully been filled and it solvable            
    return True
