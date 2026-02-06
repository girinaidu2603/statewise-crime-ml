import pandas as pd

# Load data
df = pd.read_csv("crime_data.csv")

# Basic cleaning
df.dropna(inplace=True)
df['Year'] = df['Year'].astype(int)
df['Crime_Count'] = df['Crime_Count'].astype(int)

# Save cleaned data
df.to_csv("cleaned_crime_data.csv", index=False)

print("Data cleaned successfully!")
