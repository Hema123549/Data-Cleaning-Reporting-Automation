import pandas as pd

df = pd.read_csv("sales_data.csv")

print(df.head())

import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Show original
print("Original Data:")
print(df.head())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df = df.ffill()

# Show cleaned data
print("Cleaned Data:")
print(df.head())

# Save cleaned file
df.to_csv("cleaned_data.csv", index=False)