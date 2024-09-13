import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'C:\Users\harsh\Downloads\Learn Statatics From Scratch\Stress monitoring model\Raw Data.csv')

# Check for missing values and initial statistics
df.info()
print(df.describe())

# Drop columns/rows with missing data
df_cleaned = df.dropna(axis=1)
df_cleaned = df_cleaned.dropna(axis=0)

# Impute missing values in the 'Anxiety Value' column
if 'Anxiety Value' in df.columns:
    df['Anxiety Value'] = df['Anxiety Value'].fillna(df['Anxiety Value'].mean())
    df['Anxiety_is_missing'] = df['Anxiety Value'].isnull()

# Encode categorical data in the 'City' column
if 'City' in df.columns:
    df['City'] = df['City'].fillna('Unknown')
    label_encoder = LabelEncoder()
    df['City_Label'] = label_encoder.fit_transform(df['City'])
    
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    df_city_encoded = encoder.fit_transform(df[['City']])
    df_city_encoded_df = pd.DataFrame(df_city_encoded, columns=encoder.get_feature_names_out(['City']))
    
    df = pd.concat([df, df_city_encoded_df], axis=1)

# Save processed data
df.to_csv(r'C:\Users\harsh\Downloads\Learn Statatics From Scratch\missing values and effective analysis\xsdjdms.csv', index=False)

# Basic visualizations

# 1. Distribution of Anxiety Value
plt.figure(figsize=(8, 5))
sns.histplot(df['Anxiety Value'], kde=True)
plt.title('Distribution of Anxiety Value')
plt.xlabel('Anxiety Value')
plt.ylabel('Frequency')
plt.show()

# 2. Anxiety Value by City (Boxplot)
plt.figure(figsize=(10, 6))
sns.boxplot(x='City', y='Anxiety Value', data=df)
plt.title('Anxiety Value by City')
plt.xlabel('City')
plt.ylabel('Anxiety Value')
plt.xticks(rotation=45)
plt.show()

# 3. Correlation Heatmap (if you have multiple numerical features)
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Load original data for comparison
original_df = pd.read_csv(r'C:\Users\harsh\Downloads\Learn Statatics From Scratch\Stress monitoring model\Raw Data.csv')

# Ensure both DataFrames have the same columns and indexes
common_columns = original_df.columns.intersection(df.columns)
df_aligned = df[common_columns]
original_df_aligned = original_df[common_columns]

# Ensure identical indexes
df_aligned = df_aligned.set_index(original_df.index)

# Compare with original data
comparison_df = original_df_aligned.compare(df_aligned, align_axis=1)
comparison_df.to_csv(r'C:\Users\harsh\Downloads\Learn Statatics From Scratch\missing values and effective analysis\xsdjdms.csv')