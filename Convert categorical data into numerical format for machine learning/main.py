import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv(r"C:\Users\Kuro7\Downloads\Learn-Statatics-from-scratch-main\How to perform Data formatting and normalisation\Raw Data.csv")

# 1. One-Hot Encoding for 'University'
if 'University' in df.columns:
    ohe_university = OneHotEncoder(sparse=False, handle_unknown='ignore')
    encoded_university = ohe_university.fit_transform(df[['University']])
    university_df = pd.DataFrame(encoded_university, columns=ohe_university.get_feature_names_out(['University']))
    df = pd.concat([df, university_df], axis=1)

    # Visualize University distribution
    plt.figure(figsize=(12, 6))
    sns.countplot(y='University', data=df) 
    plt.title('University Distribution')
    plt.show()
else:
    print("Warning: 'University' column not found. Skipping one-hot encoding.")

# 2. One-Hot Encoding for 'Department'
if 'Department' in df.columns:
    ohe_department = OneHotEncoder(sparse=False, handle_unknown='ignore')
    encoded_department = ohe_department.fit_transform(df[['Department']])
    department_df = pd.DataFrame(encoded_department, columns=ohe_department.get_feature_names_out(['Department']))
    df = pd.concat([df, department_df], axis=1)

    # Visualize Department distribution
    plt.figure(figsize=(12, 6)) 
    sns.countplot(y='Department', data=df)
    plt.title('Department Distribution')
    plt.show()
else:
    print("Warning: 'Department' column not found. Skipping one-hot encoding.")

# 3. Label Encoding for 'Did you receive a waiver or scholarship at your university?' 
# (Assuming it's ordinal: 'No' < 'Yes')
if 'Did you receive a waiver or scholarship at your university?' in df.columns:
    # Handle NaN values (replace with 'Unknown')
    df['Did you receive a waiver or scholarship at your university?'] = df['Did you receive a waiver or scholarship at your university?'].fillna('Unknown') 

    le = LabelEncoder()
    df['Scholarship_Encoded'] = le.fit_transform(df['Did you receive a waiver or scholarship at your university?'])

    # Visualize original and encoded distributions
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    df['Did you receive a waiver or scholarship at your university?'].value_counts().plot(kind='bar')
    plt.title('Original Scholarship Distribution')

    plt.subplot(1, 2, 2)
    df['Scholarship_Encoded'].value_counts().sort_index().plot(kind='bar')
    plt.title('Encoded Scholarship Distribution')
    plt.show()


# Numerical data analysis and visualization
anxiety_cols = df.columns[7:14]
stress_cols = df.columns[15:25]
depression_cols = df.columns[26:36]

# Convert stress columns to numeric and handle NaN
for col in stress_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df[stress_cols] = df[stress_cols].fillna(df[stress_cols].mean()) 

# Calculate mean scores
mean_anxiety = df[anxiety_cols].mean(axis=1)
mean_stress = df[stress_cols].mean(axis=1)
mean_depression = df[depression_cols].mean(axis=1)

# Visualize distributions
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
sns.histplot(mean_anxiety, kde=True)
plt.title('Anxiety Score Distribution')

plt.subplot(1, 3, 2)
sns.histplot(mean_stress, kde=True)
plt.title('Stress Score Distribution')

plt.subplot(1, 3, 3)
sns.histplot(mean_depression, kde=True)
plt.title('Depression Score Distribution')

plt.tight_layout()
plt.show()

# Explore relationships
sns.pairplot(df[['Anxiety Value', 'Stress Value', 'Depression Value']])
plt.show()

# Display summary statistics
print("\nSummary Statistics:\n", df[['Anxiety Value', 'Stress Value', 'Depression Value']].describe().to_markdown())

# Display the final DataFrame (first few rows)
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))