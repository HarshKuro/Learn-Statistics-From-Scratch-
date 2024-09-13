import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy.stats import zscore
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd


# Read the CSV file using the provided path
df = pd.read_csv(r"C:\Users\Kuro7\Downloads\Learn-Statatics-from-scratch-main\How to perform Data formatting and normalisation\Raw Data.csv")

# Clean and convert column names
df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('[^a-zA-Z0-9_]', '', regex=True)

# Convert `6_Current_CGPA` to numeric, coercing non-numeric values to NaN
df['6_Current_CGPA'] = pd.to_numeric(df['6_Current_CGPA'], errors='coerce')

# Select relevant numerical columns
anxiety_cols = df.columns[7:14]
stress_cols = df.columns[15:25]
depression_cols = df.columns[26:36]
numerical_cols = anxiety_cols.union(stress_cols).union(depression_cols).union(['6_Current_CGPA'])

# Filter only numeric columns and drop any remaining non-numeric columns
numerical_data = df[numerical_cols].select_dtypes(include='number')

# Impute missing values with mean
imputer = SimpleImputer(strategy='mean')
numerical_data_imputed = imputer.fit_transform(numerical_data)

# Standardize data
scaler = StandardScaler()
numerical_data_scaled = scaler.fit_transform(numerical_data_imputed)

# Perform PCA
pca = PCA(n_components=2)
data_pca = pca.fit_transform(numerical_data_scaled)
pca_df = pd.DataFrame(data_pca, columns=['PCA1', 'PCA2'])

# Calculate Z-scores
for col in numerical_data.columns:
    df[col + '_zscore'] = zscore(df[col])

# Display results
print("\nPCA Results (First 5 rows):\n", pca_df.head().to_markdown(index=False, numalign="left", stralign="left"))
print("\nData with Z-scores (First 5 rows):\n", 
      df[['6_Current_CGPA', '6_Current_CGPA_zscore'] + list(anxiety_cols) + 
         list(stress_cols) + list(depression_cols)].head().to_markdown(index=False, numalign="left", stralign="left"))


# Assuming 'pca_df' is your DataFrame
fig, ax = plt.subplots(figsize=(12, 4))  # Adjust figure size as needed
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=pca_df.values, colLabels=pca_df.columns, loc='center')

# Save to PDF
pp = PdfPages("pca_results.pdf")
pp.savefig(fig, bbox_inches='tight')
pp.close()

# Select the columns you want to save (adjust as needed)
zscore_df = df[['6_Current_CGPA', '6_Current_CGPA_zscore'] + list(anxiety_cols) + list(stress_cols) + list(depression_cols)]

# Create a figure and table
fig, ax = plt.subplots(figsize=(12, 6))  # Adjust figure size as needed
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=zscore_df.values, colLabels=zscore_df.columns, loc='center')

# Save to PDF
pp = PdfPages("zscore_results.pdf")
pp.savefig(fig, bbox_inches='tight')
pp.close()