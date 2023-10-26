from preprocess_data import preprocess_data, preprocess_data_2D
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
from keras.utils import to_categorical


# Use the file path to your CSV file
file_path = 'C:/Users/ramosv/Desktop/Github/Sudoku-Game/sudoku.csv'

X_train, X_test, y_train, y_test = preprocess_data(file_path)

model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)
print(f"RandomForestClassifier Model accuracy: {accuracy}")
print("RandomForestClassifier Classification report:")
print(classification_report(y_test,y_pred))


### CNN

X_train, X_test, y_train, y_test = preprocess_data_2D(file_path)

#print("Shape of y_train:", np.array(y_train).shape)
#print("Shape of y_test:", np.array(y_test).shape)

X_train = np.array(X_train).reshape(-1, 9, 9, 1)
X_test = np.array(X_test).reshape(-1, 9, 9, 1)

#y_train = to_categorical(y_train)
#y_test = to_categorical(y_test)
model = Sequential()
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(9, 9, 1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
#model.summary()
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test), verbose=0)
#model.summary()

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Model accuracy: {accuracy}")

# Predict the Probabilities
y_pred_prob = model.predict(X_test)

# Convert Probabilities to Class Labels
y_pred_labels = np.argmax(y_pred_prob, axis=1)

# Convert One-Hot Encoded Ground Truth to Class Labels
y_true_labels = np.argmax(y_test, axis=1)

# Generate and Print Classification Report
print("Classification report:")
print(classification_report(y_true_labels, y_pred_labels))