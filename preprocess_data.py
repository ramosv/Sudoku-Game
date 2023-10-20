import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path):
    #Load the data, only grabbing the first 10000
    data = pd.read_csv(path,nrows=10000)
    return data

#Preprocess data as grid
def preprocess_sudoku_asgrid(s):
    #Conver strings into arrays of integers
    sudoku = []

    #Loop over string in chunks of 9, len(s) = 81
    for i in range(0, len(s), 9):
        #Substring of row in sudoku grid
        row = s[i:i+9]

        #empty list for this row
        row_list = []

        #Loop over each char in substring
        for char in row:
            #Conver to int
            row_list.append(int(char))

        #Append list to grid
        sudoku.append(row_list) 
    return sudoku

def preprocess_sudoku(s):
    sudoku = []

    for char in s:
        sudoku.append(int(char))

    return sudoku

   
def process_solutions(data):
    puzzles = data['puzzle'].tolist()
    solutions = data['solution'].tolist()

    X, y = [],[]

    for p, s in zip(puzzles,solutions):
        puzzle_flat = preprocess_sudoku(p)
        solution_flat = preprocess_sudoku(s)

        #For each cell in the sudoku grid
        for i in range(81):
            X.append(puzzle_flat[:i] + [0] + puzzle_flat[i+1:])
            y.append(solution_flat[i])

    return X,y

def training_testing_data(puzzles, solutions,testSize =0.2):
    #Splitting data into training and training sets
    X_train, X_test, y_train, y_test = train_test_split(puzzles, solutions, test_size=testSize, random_state=42)
    return X_train, X_test, y_train, y_test

def preprocess_data(path):
    data = load_data(path)
    puzzles, solutions = process_solutions(data)

    #Training and testing data for model
    return training_testing_data(puzzles,solutions)






