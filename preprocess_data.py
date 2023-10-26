import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

##### Preprocess data to be used in a RandomForestClassifier Model #####
def load_data(path):
    #Load the data, only grabbing the first 10000
    data = pd.read_csv(path,nrows=2000)
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

#### Pre-processing Data to be represented as a 2D grid to be used in a Convolutional Neural Network(CNN)

def preprocess_sudoku2D(s):
    #Conver things into 2D arrays of strings
    return [list(map(int, list(s[i:i+9]))) for i in range(0, len(s), 9)]
def process_solutions_2D(data):
    puzzles = data['puzzle'].tolist()
    solutions = data['solution'].tolist()

    X, y = [], []

    for p, s in zip(puzzles, solutions):
        puzzle_grid = preprocess_sudoku2D(p)
        solution_grid = preprocess_sudoku2D(s)

        # Loop over each cell in the sudoku grid
        for i in range(9):
            for j in range(9):
                # Make a deep copy of the puzzle grid
                modified_puzzle = [row.copy() for row in puzzle_grid]
                # Blank out the cell we are trying to predict
                modified_puzzle[i][j] = 0
                
                X.append(modified_puzzle)

                #print("Value to be encoded:", solution_grid[i][j])

                # We use to_categorical to convert the number into one-hot encoding
                encoded_cell = to_categorical(solution_grid[i][j], num_classes=10)
                #print("Shape of encoded cell:", encoded_cell.shape)
                y.append(encoded_cell)

    y = np.array(y)
    #print("Shape of y:", y.shape)

    return X, y


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
    # print("Shape of X_train:", np.array(X_train).shape)
    # print("Shape of X_test:", np.array(X_test).shape)
    # print("Shape of y_train:", np.array(y_train).shape)
    # print("Shape of y_test:", np.array(y_test).shape)

    return X_train, X_test, y_train, y_test


#### RandomForestClassifier Model #####
def preprocess_data(path):
    data = load_data(path)
    puzzles, solutions = process_solutions(data)

    #Training and testing data for model
    return training_testing_data(puzzles,solutions)

#### Convolutional Neural Network(CNN)
def preprocess_data_2D(path):
    data = load_data(path)
    puzzles, solutions = process_solutions_2D(data)

    # Training and testing data for model
    return training_testing_data(puzzles, solutions)








