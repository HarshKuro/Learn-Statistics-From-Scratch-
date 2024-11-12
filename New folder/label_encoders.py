import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import category_encoders as ce

# Sample data
data = {'Color': ['Red', 'Blue', 'Green', 'Blue', 'Green', 'Red']}
df = pd.DataFrame(data)

# Label Encoding
label_encoder = LabelEncoder()
df['Color_Label'] = label_encoder.fit_transform(df['Color'])
print("Label Encoding:\n", df)

# One-Hot Encoding
one_hot_encoder = OneHotEncoder(sparse_output=False)  # 'sparse=False' deprecated in newer versions
one_hot_encoded = one_hot_encoder.fit_transform(df[['Color']])
df_one_hot = pd.DataFrame(one_hot_encoded, columns=one_hot_encoder.get_feature_names_out(['Color']))
print("\nOne-Hot Encoding:\n", pd.concat([df, df_one_hot], axis=1))

# Binary Encoding
binary_encoder = ce.BinaryEncoder(cols=['Color'])
df_binary = binary_encoder.fit_transform(df)
print("\nBinary Encoding:\n", df_binary)