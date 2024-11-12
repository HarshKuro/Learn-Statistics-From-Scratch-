import pandas as pd

# Load the iris dataset
df = pd.read_csv(r'C:\Users\Kuro7\Downloads\Learn-Statatics-from-scratch-main\iris 9th\Iris.csv')

# Drop the column `Id`
df = df.drop(columns='Id')

# Filter data for each species
setosa = df[df['Species'] == 'Iris-setosa']
versicolor = df[df['Species'] == 'Iris-versicolor']
virginica = df[df['Species'] == 'Iris-virginica']

# Function to display basic statistical details
def display_stats(data, species_name):
    print(f"Statistics for {species_name}:")
    print(data.describe())
    print('-' * 40)

# Display stats for each species
display_stats(setosa.drop(columns='Species'), 'Iris-setosa')
display_stats(versicolor.drop(columns='Species'), 'Iris-versicolor')
display_stats(virginica.drop(columns='Species'), 'Iris-virginica')