from preprocess_data import preprocess_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Use the file path to your CSV file
file_path = 'C:/Users/ramosv/Desktop/Github/Sudoku-Game/sudoku.csv'

X_train, X_test, y_train, y_test = preprocess_data(file_path)

model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)
print(f"Model accuracy: {accuracy}")
print("Classification report:")
print(classification_report(y_test,y_pred))
