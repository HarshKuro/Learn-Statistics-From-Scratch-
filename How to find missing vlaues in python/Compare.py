import pandas as pd
import os

# Load the original dataset
original_df = pd.read_csv(r'C:\Users\harsh\Downloads\Stats second year 3rd sem\Stress monitoring model\Raw Data.csv')

# Load the new (processed) dataset
processed_df = pd.read_csv(r'C:\Users\harsh\Downloads\Learn Statatics From Scratch\How to find missing vlaues in python\Processed_Data.csv')

# Check if the dimensions of the datasets are the same
if original_df.shape != processed_df.shape:
    print("The datasets have different shapes.")
    print(f"Original Dataset Shape: {original_df.shape}")
    print(f"Processed Dataset Shape: {processed_df.shape}")
else:
    print("The datasets have the same shape.")

# Compare the data
comparison_df = original_df.compare(processed_df, align_axis=1, keep_shape=True, keep_equal=True)

# Display the comparison results
print("\nComparison between original and processed data:")
print(comparison_df)

# Save the comparison results to a CSV file
comparison_file = os.path.join(r'C:\Users\harsh\Downloads\Learn Statatics From Scratch\How to find missing vlaues in python', 'Comparison_Results.csv')
comparison_df.to_csv(comparison_file)

print(f"\nComparison results saved to {comparison_file}")
