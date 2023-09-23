##Algorithm to check if sudoku game is legal

##I will be deviding this into 3 functions


##First checking if the row in matrix is legal
##For a row in sudoku to be legal, all 9 numbers must be unique from 1-9

def row_correct(sudoku: list,row_no:int):

    ##List.count(i) returns the number of times i is seen on     the list.
    for number in sudoku[row_no]:
        if sudoku[row_no].count(number) > 1 and number is not 0:
            return False
    return True

##Next step is to check if a column is legal

def column_correct(sudoku:list,column_no:int):
    numbers= []

    ##row[column_no] look at each row at index column_no
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in numbers:
            return False
        numbers.append(row[column_no])
    
    return True

##Next is to check each block.
##There are 9 block in sudoku and each bock must follow the same rules as above
##Row and Col will be passed as parameters to see which block we are checking.
##Block star on the top left at the following locations of the matrix
## (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3),(6, 6)
def block_correct(sudoku:list, row, col):
    block = []

    for i in range(row,row+3):
        for j in range(col,col+3):

            number = sudoku[i][j]

            if number > 0 and number in block:
                return False
            
            block.append(number)

    return True

##Using the functions built above, I can check the entire grid for illegal moves
def sudoku_grid_correct(sudoku:list):
    blocks = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3),(6, 6)]

    for i in range(0,9):
        row = row_correct(sudoku,i)
        column = column_correct(sudoku,i)

        if not row or not column:
            return False
        
    for i in blocks:
        block = block_correct(sudoku,i[0],i[1])
        ##If any of the functions retuns False, an ilegal move has been made
        if not block:
            return False

    
    return True

if __name__ == "__main__":

    ##FALSE,TRUE,FALSE
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))

    sudoku3 = [
    [6, 4, 9, 2, 8, 3, 1, 5, 7],
    [0, 5, 0, 6, 4, 9, 2, 3, 8],
    [2, 3, 8, 1, 5, 7, 6, 4, 9],
    [9, 2, 3, 8, 1, 5, 0, 6, 4],
    [7, 6, 4, 9, 2, 3, 8, 1, 5],
    [8, 1, 5, 7, 0, 4, 9, 2, 0],
    [5, 7, 6, 4, 9, 2, 3, 2, 1],
    [4, 0, 2, 3, 8, 1, 5, 0, 6],
    [3, 0, 1, 5, 0, 6, 4, 9, 0],
    ]
    print(sudoku_grid_correct(sudoku3))