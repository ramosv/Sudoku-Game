from printboard import *
import checking
import random

def print_sudoku(sudoku:list):
    row = 0

    for rows in sudoku:
        block = 0

        for number in rows:
            block +=1

            if number == 0:
                number = "_"
            new = f"{number}"

            if block % 3 == 0 and block < 8:
                new += " "

            print(new, end="")

        print()
        row+=1
        if row%3 == 0 and row < 8:
            print()


def add_number(sudoku, row, column, num):
    sudoku[row][column] = num

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copy_sudoku = [row[:] for row in sudoku]
    add_number(copy_sudoku,row_no,column_no,number)
    return copy_sudoku

def isZero(sudoku,row,col):
    num = sudoku[row][col]

    return num == 0

def new_game():
    ##Minimum number for a sudoku game to start with is 17
    ##I will start the game with 25 to make it easier   
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    idx = 0
    while idx < 20:
        row = random.randint(0,8)
        column = random.randint(0,8)

        newNumber = random.randint(1,9)

        ##Adding to number to a copy to make sure it is legal add.
        empty = isZero(sudoku,row,column) 
        if empty:
            grid_copy = copy_and_add(sudoku,row,column,newNumber)
        else:
            continue
        
        if checking.sudoku_grid_correct(grid_copy) != False and empty != False:
            add_number(sudoku, row,column,newNumber)
            idx+=1
        else:
            continue   

    return sudoku


def main():
    ##Once every space has been filled, the total sum should be 1215
    masterSum = 0
    lives = 5

    #while masterSum < 1215 and lives > 0:
    
    sudoku = new_game()

    print_sudoku(sudoku)





main()
    

