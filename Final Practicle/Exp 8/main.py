import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Generate Dataset
np.random.seed(42)
data = {'Value': np.random.normal(50, 10, 100).tolist() + [100, 120, 130]}  # Add outliers
df = pd.DataFrame(data)

# 2. Calculate Quartiles and IQR
Q1 = df['Value'].quantile(0.25)
Q3 = df['Value'].quantile(0.75)
IQR = Q3 - Q1

# 3. Define Bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# 4. Identify Outliers
outliers = ((df['Value'] < lower_bound) | (df['Value'] > upper_bound))

# 5. Handle Outliers (Choose ONE method)

# 5.1 Remove Outliers
df_removed = df[~outliers]

# 5.2 Cap Outliers
df_capped = df.copy()
df_capped['Value'] = np.clip(df_capped['Value'], lower_bound, upper_bound)

# 5.3 Transform Data (Log Transformation)
df_transformed = df.copy()
df_transformed['Value'] = np.log1p(df_transformed['Value'])

# Visualize
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
df['Value'].hist(bins=10)
plt.title('Original Data')
plt.subplot(1, 4, 2)
df_removed['Value'].hist(bins=10)
plt.title('Outliers Removed')
plt.subplot(1, 4, 3)
df_capped['Value'].hist(bins=10)
plt.title('Outliers Capped')
plt.subplot(1, 4, 4)
df_transformed['Value'].hist(bins=10)
plt.title('Log Transformed')
plt.show() 