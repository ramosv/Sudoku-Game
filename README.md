# Sudoku-Game built from scratch in python
* On going project to develop a Sudoku Game solver that uses machine learning to solve any Sudoku game
* Developed an algorithm to detect if a given sudoku game board is legal and solvable.
* Built a model that can solve sudoku puzzles with low accuracy.
* Next step is try different models and compare their accuracy with the existing baseline

## Solving the puzzle
Sudoku is a logical and rule based puzzle game. It not simply just in pattern recognition. Machine learning models, such as Random Forests and Convolutional Neural networks are built to recognize patter. They are unable to learn the rules of the game by just looking at solved sudoky games. Training on "apperance" is not an effective way to approach this problem, as it is unable to capture the logical structure of the problem.

With that being said, the most effective and commonly known method for solving sudoku puzzles is using backtracking algorithms. Backtracking works by trying a potential solution, then if it does not work, we backtrack to the previous know "legal puzzle". Trying out different possibilities while checking these possibilities with the known rules of the game will lead us to complete the puzzle.

Purpose of this project was to test common machine learning algothims and figure why they perform the way they do with a problem like Sudoku. Which problems are the machine learning algorithms best suited for and why? are some of the questions I would like answer as we move forward in the project.


## Testing with 2000 combinations of puzzles and solutions
### Data came from https://www.kaggle.com/datasets/rohanrao/sudoku

### Evaluating classification reports
* Precision: Accuracy of positive predictions
* Recall: Ratio of positive instances corretly detected
* F1-Score: Harmonic mean of precision and recall. Where a value of 1 means perfect precision and recall
* Support: Value of occurances of the class in the specified dataset

### Random Forest
The sample data is quite small being used is small, but it provides an insight in to how this model would perform.

It seem the results are almost random, in fact it is performing slightly worst than completely random.
Where random guessing would give us a around 11% accuracy

The training data may very well be directly correlated to these results. More data may give us a result closet to 11%


RandomForestClassifier Model accuracy: 0.07074074074074074
RandomForestClassifier Classification report:
              precision    recall  f1-score   support

           1       0.07      0.07      0.07      3565
           2       0.07      0.06      0.06      3638
           3       0.07      0.06      0.06      3633
           4       0.07      0.07      0.07      3616
           5       0.07      0.07      0.07      3614
           6       0.06      0.07      0.06      3497
           7       0.07      0.07      0.07      3641
           8       0.07      0.08      0.08      3561
           9       0.09      0.10      0.09      3635

    accuracy                           0.07     32400
   macro avg       0.07      0.07      0.07     32400
weighted avg       0.07      0.07      0.07     32400


### CNN

Precision,recall and f1-scores have more variation in comparison to RandomForest model. Class 1 and 9 have higher prediction while other not so much.

12% is slightly higher than 7% but still very low.


CNN
Classification report:
              precision    recall  f1-score   support

           1       0.12      0.47      0.19     14400
           2       0.11      0.00      0.00     14400
           3       0.11      0.06      0.08     14400
           4       0.10      0.02      0.03     14400
           5       0.11      0.05      0.07     14400
           6       0.00      0.00      0.00     14400
           7       0.09      0.00      0.00     14400
           8       0.12      0.00      0.01     14400
           9       0.13      0.46      0.20     14400

    accuracy                           0.12    129600
   macro avg       0.10      0.12      0.06    129600
weighted avg       0.10      0.12      0.06    129600


Summary and questions.
Both models are not performing well, CNN performs slightly better than randomly guessing.Models may not be representing the data, indicating that the nature of these models may not be suited for this task. It seems like they are struggling to understand the rules of the game.

Now is there a way to incorporate the rules of the game into the models?

Would hybrid approach between backtracking algorithm and one of these models be a solution?

Is a different model better suited? Maybe RNNs
Recurrent Neutal Netoworks(RNNs): are able to handle sequences and retail memory. This model may perform better than CNN and RandomForest.