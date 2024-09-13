import numpy as np 
import pandas as pd 
import statistics 
import math 
import scipy.stats as st
data = pd.read_csv(r"C:\Users\harsh\Downloads\Stats second year 3rd sem\Second exp\housing.csv")

# Get numerical columns
numerical_columns = data.select_dtypes(include='number')

# 1. Display the first 5 rows
print("First 5 rows:")
print(data.head().to_markdown(index=False, numalign="left", stralign="left"))

# 2. Display the last 5 rows
print("\nLast 5 rows:")
print(data.tail().to_markdown(index=False, numalign="left", stralign="left"))

# Function to calculate stats using different libraries
def calculate_stats(series, lib='pandas'):
    if lib == 'pandas':
        return series.agg(['count', 'sum', 'max', 'min'])
    elif lib == 'numpy':
        return pd.Series({
            'count': np.count_nonzero(~np.isnan(series)),
            'sum': np.nansum(series),
            'max': np.nanmax(series),
            'min': np.nanmin(series)
        })
    elif lib == 'statistics':
        return pd.Series({
            'count': len(series),
            'sum': series.sum(),
            'max': series.max(),
            'min': series.min()
        })

# 3. Count, sum, max, min for each library
for lib in ['pandas', 'numpy', 'statistics']:
    print(f"\nCount, sum, max, min using {lib}:")
    print(numerical_columns.apply(calculate_stats, lib=lib).to_markdown())

# Function to describe data using different libraries
def describe_data(series, lib='pandas'):
    if lib == 'pandas':
        return series.describe()
    elif lib == 'numpy':
        return pd.Series({
            'count': np.count_nonzero(~np.isnan(series)),
            'mean': np.nanmean(series),
            'std': np.nanstd(series),
            'min': np.nanmin(series),
            '25%': np.nanpercentile(series, 25),
            '50%': np.nanpercentile(series, 50),
            '75%': np.nanpercentile(series, 75),
            'max': np.nanmax(series)
        })

# 4. Descriptive statistics
for lib in ['pandas', 'numpy']:
    print(f"\nDescriptive statistics using {lib}:")
    print(numerical_columns.apply(describe_data, lib=lib).to_markdown())

# 5. Skewness
print("\nSkewness:")
print(numerical_columns.apply(st.skew).rename("Skewness").to_markdown(numalign="left", stralign="left"))

# 6. Correlation matrix
print("\nCorrelation matrix:")
print(numerical_columns.corr(method='pearson').to_markdown())

# 7. Standard deviation
print("\nStandard deviation:")
print(numerical_columns.std().rename("Std Deviation").to_markdown(numalign="left", stralign="left"))

