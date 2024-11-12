import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv(r"C:\Users\Kuro7\Downloads\Learn-Statatics-from-scratch-main\Final Practicle\Exp 3\titanic.csv")

# Display initial info
print(data.head())
print(data.info())
print(data.describe())

# Check for missing values
print(data.isnull().sum())

# Drop rows with any missing values (dropna)
data_dropped = data.dropna()

# Fill missing values in 'Age' with mean (fillna)
data['Age'].fillna(data['Age'].mean(), inplace=True)

# Simple Imputation for 'Embarked' (most frequent)
embarked_imputer = SimpleImputer(strategy='most_frequent')
data['Embarked'] = embarked_imputer.fit_transform(data[['Embarked']])

# KNN Imputation for 'Fare'
fare_imputer = KNNImputer(n_neighbors=5)
data['Fare'] = fare_imputer.fit_transform(data[['Fare']])

# Regression Imputation for 'Age' (alternative - on original data)
lr = LinearRegression()
testdf = data[data['Age'].isnull()]
traindf = data[data['Age'].notnull()]
y = traindf['Age']
traindf.drop("Age", axis=1, inplace=True)
lr.fit(traindf, y)
testdf.drop("Age", axis=1, inplace=True)
pred = lr.predict(testdf)
testdf['Age'] = pred
data_regressed = pd.concat([traindf, testdf], axis=0)  # Combine data

# Display data after different imputation methods
print("\nData after dropping rows with missing values:")
print(data_dropped.head())
print("\nData after filling missing 'Age' with mean:")
print(data.head())
print("\nData after regression imputation for 'Age':")
print(data_regressed.head())

# Check dimensions
print("\nOriginal data dimensions:", data.shape)
print("Data dimensions after dropping rows:", data_dropped.shape)