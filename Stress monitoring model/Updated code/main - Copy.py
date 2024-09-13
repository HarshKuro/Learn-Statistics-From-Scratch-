import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'C:\Users\harsh\Downloads\Stats second year 3rd sem\Stress monitoring model\Raw Data.csv')

# Shorten university names
df['3. University'] = df['3. University'].replace({
    'Independent University, Bangladesh (IUB)': 'IUB',
    'University of Dhaka (DU)': 'DU',
})

# Create output folder
output_folder = '/mnt/data/plots'
os.makedirs(output_folder, exist_ok=True)

# Group data
grouped_data = df.groupby(['2. Gender', '3. University', '5. Academic Year'])[['Anxiety Value', 'Stress Value', 'Depression Value']].mean().reset_index()

# Bar Charts
for col in ['2. Gender', '3. University', '5. Academic Year']:
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))
    for i, metric in enumerate(['Anxiety Value', 'Stress Value', 'Depression Value']):
        axs[i].bar(grouped_data[col], grouped_data[metric], color=['skyblue', 'lightgreen', 'lightcoral'][i], edgecolor='black')
        axs[i].set_title(f'Average {metric} by {col}')
        axs[i].set_xlabel(col)
        axs[i].set_ylabel(f'Average {metric}')
        axs[i].tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, f'bar_chart_{col}.png'))
    plt.show()

# Histograms
df[['Anxiety Value', 'Stress Value', 'Depression Value']].hist(bins=20, edgecolor='black', figsize=(18, 5))
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'histograms.png'))
plt.show()

# Scatter Plots
sns.pairplot(df, vars=['Anxiety Value', 'Stress Value', 'Depression Value'], kind='scatter', plot_kws={'alpha': 0.5})
plt.savefig(os.path.join(output_folder, 'scatter_plots.png'))
plt.show()

# Line Graphs over time (Academic Year)
df['5. Academic Year'] = pd.Categorical(df['5. Academic Year'], categories=['First Year or Equivalent', 'Second Year or Equivalent', 'Third Year or Equivalent', 'Fourth Year or Equivalent'], ordered=True)
grouped_time = df.groupby('5. Academic Year')[['Anxiety Value', 'Stress Value', 'Depression Value']].mean()
grouped_time.plot(marker='o', linestyle='-', figsize=(10, 6))
plt.title('Mental Health Metrics Over Academic Years')
plt.ylabel('Average Value')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'line_graphs.png'))
plt.show()

# Heatmaps
fig, axs = plt.subplots(1, 3, figsize=(18, 5))
for i, metric in enumerate(['Anxiety Value', 'Stress Value', 'Depression Value']):
    sns.heatmap(df.pivot_table(index='5. Academic Year', columns='2. Gender', values=metric, aggfunc='mean'), annot=True, cmap="YlGnBu", ax=axs[i])
    axs[i].set_title(f'{metric} Heatmap')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'heatmaps.png'))
plt.show()

# Box Plots
for col in ['2. Gender', '3. University', '5. Academic Year']:
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))
    for i, metric in enumerate(['Anxiety Value', 'Stress Value', 'Depression Value']):
        sns.boxplot(x=col, y=metric, data=df, ax=axs[i])
        axs[i].set_title(f'{metric} by {col}')
        axs[i].tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, f'box_plot_{col}.png'))
    plt.show()

# Summary Statistics
summary_stats = df[['Anxiety Value', 'Stress Value', 'Depression Value']].describe()
print("\nSummary Statistics:\n", summary_stats)
