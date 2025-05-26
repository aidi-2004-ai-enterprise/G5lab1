import pandas as pd
import seaborn as sns

# Load penguins dataset
penguins = sns.load_dataset("penguins")
print(penguins.head())