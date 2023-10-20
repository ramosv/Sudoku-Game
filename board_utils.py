import random
import solver

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


def remove_numbers(sudoku, number_of_cells):
    #Removing random numbers from a board to create a game
    #remove replresents the number of squares to be deleted to generate the puzzle

    count = 0
    while count < number_of_cells:
        row = random.randint(0, 8)
        col = random.randint(0,8)

        #Check if cell is empty
        if sudoku[row][col] != 0:
            sudoku[row][col] = 0
            count+=1

    return sudoku



