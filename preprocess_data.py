import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit
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
def normalize_sudoku(sudoku):
    return np.array(sudoku) / 9.0

def augment_data(puzzle, solution):
    augmented_puzzles = [puzzle, np.rot90(puzzle), np.fliplr(puzzle), np.flipud(puzzle)]
    augmented_solutions = [solution, np.rot90(solution), np.fliplr(solution), np.flipud(solution)]
    return augmented_puzzles, augmented_solutions

def stratified_train_test_split(X, y, testSize=0.2):
    sss = StratifiedShuffleSplit(n_splits=1, test_size=testSize, random_state=42)
    for train_index, test_index in sss.split(X, y):
        X_train, X_test = np.array(X)[train_index], np.array(X)[test_index]
        y_train, y_test = np.array(y)[train_index], np.array(y)[test_index]
    return X_train, X_test, y_train, y_test

def preprocess_sudoku2D(s):
    #Conver things into 2D arrays of strings
    return [list(map(int, list(s[i:i+9]))) for i in range(0, len(s), 9)]


def process_solutions_2D(data):
    puzzles = data['puzzle'].tolist()
    solutions = data['solution'].tolist()

    X, y = [], []

    for p, s in zip(puzzles, solutions):
        puzzle_grid = normalize_sudoku(preprocess_sudoku2D(p))
        solution_grid = preprocess_sudoku2D(s)

        augmented_puzzles, augmented_solutions = augment_data(puzzle_grid, solution_grid)

        for aug_puzzle, aug_solution in zip(augmented_puzzles, augmented_solutions):
            for i in range(9):
                for j in range(9):
                    modified_puzzle = [row.copy() for row in aug_puzzle]
                    modified_puzzle[i][j] = 0

                    X.append(modified_puzzle)

                    encoded_cell = to_categorical(aug_solution[i][j], num_classes=10)
                    y.append(encoded_cell)

    y = np.array(y)

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
    return stratified_train_test_split(puzzles, solutions)








