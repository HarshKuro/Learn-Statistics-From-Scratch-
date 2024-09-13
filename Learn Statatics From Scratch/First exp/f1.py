import pandas as pd
import numpy as np
import statistics
data = pd.Series([2, 4, 5, 8, 10, 12, 15, 22, 25])
print("data = 2, 4, 5, 8, 10, 12, 15, 22, 25")

# 1. Mean
mean_value = np.mean(data)
print(f"Mean: {mean_value}")

# 2. Median
median_value = np.median(data)
print(f"Median: {median_value}")

# 3. Mode
mode_value = statistics.mode(data)
print(f"Mode: {mode_value}")

# 4. Standard Deviation
std_dev_value = np.std(data)
print(f"Standard Deviation: {std_dev_value}")

# 5. Variance
variance_value = np.var(data)
print(f"Variance: {variance_value}")

# 6. Sorting (Ascending)
sorted_data = np.sort(data)
print(f"Sorted Data: {sorted_data}")

# 7. Minimum
min_value = np.min(data)
print(f"Minimum: {min_value}")

# 8. Maximum
max_value = np.max(data)
print(f"Maximum: {max_value}")

# 9. Harmonic Mean
harmonic_mean_value = statistics.harmonic_mean(data)
print(f"Harmonic Mean: {harmonic_mean_value}")

# 10. Geometric Mean
geometric_mean_value = statistics.geometric_mean(data)
print(f"Geometric Mean: {geometric_mean_value}")

# 11. Percentile (e.g., 75th percentile)
percentile_75 = np.percentile(data, 75)
print(f"75th Percentile: {percentile_75}")

# 12. Skewness
skewness_value = data.skew() 
print(f"Skewness: {skewness_value}")
