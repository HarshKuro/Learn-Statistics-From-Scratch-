import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (assuming it's in a CSV file)
data = pd.read_csv(r"C:\Users\Kuro7\Downloads\Learn-Statatics-from-scratch-main\Final Practicle\Exp 3\titanic.csv")

# Display basic information
print(data.head())
print(data.info())
print(data.describe())

# Separate numerical and categorical variables
cat_cols = data.select_dtypes(include=['object']).columns
num_cols = data.select_dtypes(include=np.number).columns.tolist()
print("Categorical Variables:", cat_cols)
print("Numerical Variables:", num_cols)

# Univariate analysis (histograms and box plots for numerical variables)
for col in num_cols:
    print(col)
    print('Skew :', round(data[col].skew(), 2))
    plt.figure(figsize=(15, 4))
    plt.subplot(1, 2, 1)
    data[col].hist(grid=False)
    plt.ylabel('count')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=data[col])
    plt.show()

# Univariate analysis (count plots for categorical variables)
for col in cat_cols:
    plt.figure(figsize=(10, 4))
    sns.countplot(x=data[col])
    plt.show()

# Bivariate analysis (example: correlation heatmap for numerical variables)
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.show()