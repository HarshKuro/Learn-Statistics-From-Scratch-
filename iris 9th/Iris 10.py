import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# Load the iris dataset
df = pd.read_csv(r"C:\Users\Kuro7\Downloads\Learn-Statatics-from-scratch-main\iris 9th\Iris.csv")

# Drop the column `Id`
df = df.drop(columns='Id')

# Store the values of the columns `SepalLengthCm`, `SepalWidthCm`, `PetalLengthCm`, `PetalWidthCm`
# in `X` and the values of `Species` in `y`
X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = df['Species']

# Split the dataset into training and testing sets using the `train_test_split`
# function with 80% of the data for training and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Naïve Bayes classifier using `GaussianNB()`
nb_classifier = GaussianNB()

# Train the classifier on the training data using the `fit` method
nb_classifier.fit(X_train, y_train)

# Predict the labels for the test set using the `predict` method
y_pred = nb_classifier.predict(X_test)

# Calculate the accuracy score using the `accuracy_score` method
accuracy = accuracy_score(y_test, y_pred)

# Print the classification report using the `classification_report` method
report = classification_report(y_test, y_pred)

# Display the accuracy score
print(f'Accuracy: {accuracy}')

# Display the classification report
print(f'Classification Report: \n{report}')