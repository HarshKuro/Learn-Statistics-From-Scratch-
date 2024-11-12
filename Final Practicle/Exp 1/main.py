import numpy as np
from scipy import stats

# Sample data
data = [10, 20, 20, 30, 40, 40, 40, 50, 60]

# Mean
mean_value = np.mean(data)
print(f"Mean: {mean_value}")

# Median
median_value = np.median(data)
print(f"Median: {median_value}")

# Mode
mode_value = stats.mode(data)
print(f"Mode: {mode_value.mode[0]} (appears {mode_value.count[0]} times)")

# Variance
variance_value = np.var(data, ddof=1)  # ddof=1 for sample variance
print(f"Variance: {variance_value}")

# Standard Deviation
std_deviation_value = np.std(data, ddof=1)  # ddof=1 for sample standard deviation
print(f"Standard Deviation: {std_deviation_value}")