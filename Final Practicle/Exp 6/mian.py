import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import category_encoders as ce

# Load the dataset
data = pd.read_csv('titanic.csv')

# Display information about the dataset
print("First 5 rows of the dataset:")
print(data.head())
print("\nColumn information:")
print(data.info())

# Select categorical features for encoding
categorical_features = ['Sex', 'Embarked']

# 1. Label Encoding
label_encoder = LabelEncoder()
for feature in categorical_features:
    data[feature + '_label'] = label_encoder.fit_transform(data[feature])
    print(f"\nUnique values of {feature}: {data[feature].unique()}")
    print(f"Unique values of {feature}_label: {data[feature + '_label'].unique()}")

# 2. One-Hot Encoding
onehot_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoded_data = onehot_encoder.fit_transform(data[categorical_features])
encoded_df = pd.DataFrame(encoded_data,
                          columns=onehot_encoder.get_feature_names_out(categorical_features))
data = pd.concat([data, encoded_df], axis=1)
print("\nOne-hot encoded columns:\n", encoded_df.head())

# 3. Binary Encoding
binary_encoder = ce.BinaryEncoder(cols=categorical_features)
data = binary_encoder.fit_transform(data)
print("\nBinary encoded columns:\n", data[['Sex_0', 'Sex_1', 'Embarked_0', 'Embarked_1']].head())

# Display the encoded data
print("\nEncoded data:")
print(data.head())