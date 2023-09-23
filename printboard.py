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


