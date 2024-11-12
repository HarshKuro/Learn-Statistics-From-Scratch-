import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# Load the dataset
data = pd.read_csv('titanic.csv')

# 1. Missing Values
print("Missing values per column:")
print(data.isnull().sum())

# Impute missing values (using SimpleImputer)
numerical_features = ['Age', 'Fare']
imputer = SimpleImputer(strategy='mean')
data[numerical_features] = imputer.fit_transform(data[numerical_features])

categorical_features = ['Embarked']
imputer = SimpleImputer(strategy='most_frequent')
data[categorical_features] = imputer.fit_transform(data[categorical_features])

# 2. Inconsistencies (Duplicates)
print("\nNumber of duplicate rows:", data.duplicated().sum())
data.drop_duplicates(inplace=True)

# 3. Outliers (Example - 'Fare')
# (Using IQR method - you might need to adjust this for your data)
Q1 = data['Fare'].quantile(0.25)
Q3 = data['Fare'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
data = data[(data['Fare'] >= lower_bound) & (data['Fare'] <= upper_bound)]

# 4. Standardization (Example - 'Age')
data['Age'] = (data['Age'] - data['Age'].mean()) / data['Age'].std()

# 5. Formatting Issues (Example - 'Name')
data['Name'] = data['Name'].str.title()  # Capitalize names

# Display the cleaned data
print("\nCleaned data:")
print(data.head())