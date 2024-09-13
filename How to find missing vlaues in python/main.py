import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv(r'C:\Users\harsh\Downloads\Stats second year 3rd sem\Stress monitoring model\Raw Data.csv')

# Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

# Use notnull to filter non-missing values
non_missing_df = df[df['Anxiety Value'].notnull() & df['Stress Value'].notnull()]

# Fill missing values with the mean of each numeric column
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df_filled = df.copy()
df_filled[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Replace specific values (example: replace negative values with NaN)
df_replaced = df.replace([-999, -1], pd.NA)

# Interpolate missing values
df_interpolated = df.interpolate()

# Check unique values in each column
unique_values = df.nunique()
print("Unique Values:\n", unique_values)

# Get information about the dataframe
df_info = df.info()

# Get column names
columns = df.columns
print("Columns:\n", columns)

# Label Encoding for categorical variables
label_encoder = LabelEncoder()
df['2. Gender'] = label_encoder.fit_transform(df['2. Gender'].fillna('Unknown'))
df['3. University'] = label_encoder.fit_transform(df['3. University'].fillna('Unknown'))

# Using iloc to select specific rows and columns
subset_df = df.iloc[:, [1, 2, 4, 5, 6]]  # Adjust columns as needed

# Saving the processed DataFrame to a new CSV file
output_folder = r'C:\Users\harsh\Downloads\Learn Statatics From Scratch\How to find missing vlaues in python'
output_file = os.path.join(output_folder, 'Processed_Data.csv')
df_filled.to_csv(output_file, index=False)

print(f"Processed data saved to {output_file}")
