import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data with outliers
np.random.seed(42)
data = {
    'Age': np.random.normal(50, 15, 100).tolist() + [120, 130, 140],  # Adding some outliers
    'Salary': np.random.normal(70000, 15000, 100).tolist() + [200000, 250000, 300000]  # Adding some outliers
}
df = pd.DataFrame(data)

# Step 1: Visualize Outliers
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['Age'])
plt.title("Boxplot for Age")

plt.subplot(1, 2, 2)
sns.boxplot(y=df['Salary'])
plt.title("Boxplot for Salary")

plt.show()

# Step 2: Detect Outliers using IQR
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# Define lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = ((df < lower_bound) | (df > upper_bound)).any(axis=1)
print("Outliers Detected:\n", df[outliers])

# Step 3: Handle Outliers - Option 1: Remove Outliers
df_no_outliers = df[~outliers]
print("\nData after removing outliers:\n", df_no_outliers.describe())

# Step 3: Handle Outliers - Option 2: Cap Outliers
df_capped = df.copy()
df_capped = np.where(df < lower_bound, lower_bound, df)
df_capped = np.where(df > upper_bound, upper_bound, df)
df_capped = pd.DataFrame(df_capped, columns=df.columns)
print("\nData after capping outliers:\n", df_capped.describe())

# Step 3: Handle Outliers - Option 3: Transform Data
df_transformed = df.copy()
df_transformed['Age'] = np.log(df_transformed['Age'].replace(0, np.nan)).fillna(0)
df_transformed['Salary'] = np.log(df_transformed['Salary'].replace(0, np.nan)).fillna(0)
print("\nData after log transformation:\n", df_transformed.describe())

# Step 4: Visualize Data after Handling Outliers
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df_no_outliers['Age'])
plt.title("Boxplot for Age (No Outliers)")

plt.subplot(1, 2, 2)
sns.boxplot(y=df_no_outliers['Salary'])
plt.title("Boxplot for Salary (No Outliers)")

plt.show()

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df_capped['Age'])
plt.title("Boxplot for Age (Capped)")

plt.subplot(1, 2, 2)
sns.boxplot(y=df_capped['Salary'])
plt.title("Boxplot for Salary (Capped)")

plt.show()

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df_transformed['Age'])
plt.title("Boxplot for Age (Transformed)")

plt.subplot(1, 2, 2)
sns.boxplot(y=df_transformed['Salary'])
plt.title("Boxplot for Salary (Transformed)")

plt.show()