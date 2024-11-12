import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('titanic.csv')

# Select numerical features for scaling (example)
numerical_features = ['Age', 'Fare']

# Create a DataFrame with only the selected features
df_num = data[numerical_features].copy()

# 1. Z-score Standardization
scaler = StandardScaler()
df_num['Age_zscore'] = scaler.fit_transform(df_num[['Age']])
df_num['Fare_zscore'] = scaler.fit_transform(df_num[['Fare']])

# 2. Min-Max Scaling
scaler = MinMaxScaler()
df_num['Age_minmax'] = scaler.fit_transform(df_num[['Age']])
df_num['Fare_minmax'] = scaler.fit_transform(df_num[['Fare']])

# 3. Max Abs Scaling
scaler = MaxAbsScaler()
df_num['Age_maxabs'] = scaler.fit_transform(df_num[['Age']])
df_num['Fare_maxabs'] = scaler.fit_transform(df_num[['Fare']])

# 4. Robust Scaling
scaler = RobustScaler()
df_num['Age_robust'] = scaler.fit_transform(df_num[['Age']])
df_num['Fare_robust'] = scaler.fit_transform(df_num[['Fare']])

# Visualize the effects (example - histograms)
plt.figure(figsize=(15, 10))

plt.subplot(2, 4, 1)
df_num['Age'].hist()
plt.title('Original Age')

plt.subplot(2, 4, 2)
df_num['Age_zscore'].hist()
plt.title('Z-score')

plt.subplot(2, 4, 3)
df_num['Age_minmax'].hist()
plt.title('Min-Max')

plt.subplot(2, 4, 4)
df_num['Age_maxabs'].hist()
plt.title('Max Abs')

plt.subplot(2, 4, 5)
df_num['Fare'].hist()
plt.title('Original Fare')

plt.subplot(2, 4, 6)
df_num['Fare_zscore'].hist()
plt.title('Z-score')

plt.subplot(2, 4, 7)
df_num['Fare_minmax'].hist()
plt.title('Min-Max')

plt.subplot(2, 4, 8)
df_num['Fare_robust'].hist()
plt.title('Robust')

plt.tight_layout()
plt.show()