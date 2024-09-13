import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset
file_path = r'C:\Users\harsh\Downloads\Stats second year 3rd sem\Stress monitoring model\Raw Data.csv'
df = pd.read_csv(file_path)

# Shorten university names
df['3. University'] = df['3. University'].replace({
    'Independent University, Bangladesh (IUB)': 'IUB',
    'University of Dhaka (DU)': 'DU',
    # Add other replacements as needed
})

# Create a folder to save the plots
output_folder = '/mnt/data/plots'
os.makedirs(output_folder, exist_ok=True)

# Group by specified columns and calculate mean of mental health metrics
grouped_data = df.groupby(['2. Gender', '3. University', '5. Academic Year'])[['Anxiety Value', 'Stress Value', 'Depression Value']].mean().reset_index()

# Plotting Bar Charts for Grouped Data
for i, col in enumerate(['2. Gender', '3. University', '5. Academic Year']):
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    # Anxiety Value Bar Plot
    axs[0].bar(grouped_data[col], grouped_data['Anxiety Value'], color='skyblue', edgecolor='black')
    axs[0].set_title(f'Average Anxiety Value by {col}')
    axs[0].set_xlabel(col)
    axs[0].set_ylabel('Average Anxiety Value')
    axs[0].tick_params(axis='x', rotation=45)

    # Stress Value Bar Plot
    axs[1].bar(grouped_data[col], grouped_data['Stress Value'], color='lightgreen', edgecolor='black')
    axs[1].set_title(f'Average Stress Value by {col}')
    axs[1].set_xlabel(col)
    axs[1].set_ylabel('Average Stress Value')
    axs[1].tick_params(axis='x', rotation=45)

    # Depression Value Bar Plot
    axs[2].bar(grouped_data[col], grouped_data['Depression Value'], color='lightcoral', edgecolor='black')
    axs[2].set_title(f'Average Depression Value by {col}')
    axs[2].set_xlabel(col)
    axs[2].set_ylabel('Average Depression Value')
    axs[2].tick_params(axis='x', rotation=45)

    # Save the plot
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, f'bar_chart_{col}.png'))
    plt.show()

# Plotting Histograms for Anxiety, Stress, and Depression Values
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# Anxiety Value Histogram
axs[0].hist(df['Anxiety Value'], bins=20, color='skyblue', edgecolor='black')
axs[0].set_title('Distribution of Anxiety Value')
axs[0].set_xlabel('Anxiety Value')
axs[0].set_ylabel('Frequency')

# Stress Value Histogram
axs[1].hist(df['Stress Value'], bins=20, color='lightgreen', edgecolor='black')
axs[1].set_title('Distribution of Stress Value')
axs[1].set_xlabel('Stress Value')
axs[1].set_ylabel('Frequency')

# Depression Value Histogram
axs[2].hist(df['Depression Value'], bins=20, color='lightcoral', edgecolor='black')
axs[2].set_title('Distribution of Depression Value')
axs[2].set_xlabel('Depression Value')
axs[2].set_ylabel('Frequency')

# Save the plot
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'histograms.png'))
plt.show()

# Scatter Plots for Anxiety, Stress, and Depression Values
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# Anxiety Value vs Stress Value
axs[0].scatter(df['Anxiety Value'], df['Stress Value'], alpha=0.5)
axs[0].set_title('Scatter Plot of Anxiety Value vs Stress Value')
axs[0].set_xlabel('Anxiety Value')
axs[0].set_ylabel('Stress Value')

# Anxiety Value vs Depression Value
axs[1].scatter(df['Anxiety Value'], df['Depression Value'], alpha=0.5)
axs[1].set_title('Scatter Plot of Anxiety Value vs Depression Value')
axs[1].set_xlabel('Anxiety Value')
axs[1].set_ylabel('Depression Value')

# Stress Value vs Depression Value
axs[2].scatter(df['Stress Value'], df['Depression Value'], alpha=0.5)
axs[2].set_title('Scatter Plot of Stress Value vs Depression Value')
axs[2].set_xlabel('Stress Value')
axs[2].set_ylabel('Depression Value')

# Save the plot
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'scatter_plots.png'))
plt.show()

# Line Graphs for Anxiety, Stress, and Depression Values over time (Academic Year)
# Convert '5. Academic Year' to ordered categorical for proper sorting on x-axis
year_order = ['First Year or Equivalent', 'Second Year or Equivalent', 'Third Year or Equivalent', 'Fourth Year or Equivalent']
df['5. Academic Year'] = pd.Categorical(df['5. Academic Year'], categories=year_order, ordered=True)

# Group by '5. Academic Year' and calculate mean of mental health metrics
grouped_data_time = df.groupby('5. Academic Year')[['Anxiety Value', 'Stress Value', 'Depression Value']].mean().reset_index()

# Plotting Line Graphs
fig, ax = plt.subplots(figsize=(10, 6))

# Anxiety Value Line Plot
ax.plot(grouped_data_time['5. Academic Year'], grouped_data_time['Anxiety Value'], marker='o', linestyle='-', color='skyblue', label='Anxiety')

# Stress Value Line Plot
ax.plot(grouped_data_time['5. Academic Year'], grouped_data_time['Stress Value'], marker='o', linestyle='-', color='lightgreen', label='Stress')

# Depression Value Line Plot
ax.plot(grouped_data_time['5. Academic Year'], grouped_data_time['Depression Value'], marker='o', linestyle='-', color='lightcoral', label='Depression')

ax.set_title('Mental Health Metrics Over Academic Years')
ax.set_xlabel('Academic Year')
ax.set_ylabel('Average Value')
ax.legend()

# Save the plot
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'line_graphs.png'))
plt.show()

# Heatmap for Anxiety, Stress, and Depression Values by 'Gender' and 'Academic Year'
heatmap_data_anxiety = df.pivot_table(index='5. Academic Year', columns='2. Gender', values='Anxiety Value', aggfunc='mean')
heatmap_data_stress = df.pivot_table(index='5. Academic Year', columns='2. Gender', values='Stress Value', aggfunc='mean')
heatmap_data_depression = df.pivot_table(index='5. Academic Year', columns='2. Gender', values='Depression Value', aggfunc='mean')

# Plotting Heatmaps
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# Anxiety Value Heatmap
sns.heatmap(heatmap_data_anxiety, annot=True, cmap="YlGnBu", ax=axs[0])
axs[0].set_title('Anxiety Value Heatmap')
axs[0].set_xlabel('Gender')
axs[0].set_ylabel('Academic Year')

# Stress Value Heatmap
sns.heatmap(heatmap_data_stress, annot=True, cmap="YlGnBu", ax=axs[1])
axs[1].set_title('Stress Value Heatmap')
axs[1].set_xlabel('Gender')
axs[1].set_ylabel('Academic Year')

# Depression Value Heatmap
sns.heatmap(heatmap_data_depression, annot=True, cmap="YlGnBu", ax=axs[2])
axs[2].set_title('Depression Value Heatmap')
axs[2].set_xlabel('Gender')
axs[2].set_ylabel('Academic Year')

# Save the plot
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'heatmaps.png'))
plt.show()

# Box Plots for Anxiety, Stress, and Depression Values by Gender, University, and Academic Year
for i, col in enumerate(['2. Gender', '3. University', '5. Academic Year']):
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    # Anxiety Value Box Plot
    sns.boxplot(x=col, y='Anxiety Value', data=df, ax=axs[0])
    axs[0].set_title(f'Anxiety Value by {col}')
    axs[0].tick_params(axis='x', rotation=45)

    # Stress Value Box Plot
    sns.boxplot(x=col, y='Stress Value', data=df, ax=axs[1])
    axs[1].set_title(f'Stress Value by {col}')
    axs[1].tick_params(axis='x', rotation=45)

    # Depression Value Box Plot
    sns.boxplot(x=col, y='Depression Value', data=df, ax=axs[2])
    axs[2].set_title(f'Depression Value by {col}')
    axs[2].tick_params(axis='x', rotation=45)

    # Save the plot
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, f'box_plot_{col}.png'))
    plt.show()

# Calculate summary statistics for Anxiety, Stress, and Depression Values
summary_stats = df[['Anxiety Value', 'Stress Value', 'Depression Value']].describe()

# Calculate additional statistics
additional_stats = {
    'Mode': df[['Anxiety Value', 'Stress Value', 'Depression Value']].mode().iloc[0],
    'Variance': df[['Anxiety Value', 'Stress Value', 'Depression Value']].var(),
    'Range': df[['Anxiety Value', 'Stress Value', 'Depression Value']].max() - df[['Anxiety Value', 'Stress Value', 'Depression Value']].min(),
    'Skewness': df[['Anxiety Value', 'Stress Value', 'Depression Value']].skew(),
    'Kurtosis': df[['Anxiety Value', 'Stress Value', 'Depression Value']].kurt()
}

# Combine summary statistics with additional statistics
full_stats = summary_stats.append(additional_stats)
print("\nFull Summary Statistics:\n", full_stats)
