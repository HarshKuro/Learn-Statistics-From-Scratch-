import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy.stats import zscore
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Data Loading and Cleaning
df = pd.read_csv(r"C:\Users\Kuro7\Downloads\Learn-Statatics-from-scratch-main\How to perform Data formatting and normalisation\Raw Data.csv")
df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('[^a-zA-Z0-9_]', '', regex=True)
df['6_Current_CGPA'] = pd.to_numeric(df['6_Current_CGPA'], errors='coerce')

# Select Numerical Columns and Impute
numerical_cols = df.columns[7:14].union(df.columns[15:25]).union(df.columns[26:36]).union(['6_Current_CGPA'])
numerical_data = df[numerical_cols].select_dtypes(include='number')
numerical_data_imputed = SimpleImputer(strategy='mean').fit_transform(numerical_data)

# Standardize and Calculate Z-scores
numerical_data_scaled = StandardScaler().fit_transform(numerical_data_imputed)
for col in numerical_data.columns:
    df[col + '_zscore'] = zscore(df[col])

# PCA
pca_df = pd.DataFrame(PCA(n_components=2).fit_transform(numerical_data_scaled), columns=['PCA1', 'PCA2'])

# Display and Save Results
print(pca_df.head().to_markdown(index=False, numalign="left", stralign="left"))
zscore_cols = [col + '_zscore' for col in numerical_data.columns]
print(df[['6_Current_CGPA'] + zscore_cols + list(numerical_cols)].head().to_markdown(index=False, numalign="left", stralign="left"))



# PCA Scatter Plot
plt.scatter(pca_df['PCA1'], pca_df['PCA2'])
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.title('PCA Scatter Plot')
plt.show()