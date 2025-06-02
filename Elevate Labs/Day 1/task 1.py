import pandas as pd

# Load the dataset
df = pd.read_csv(r"Day 1\netflix_titles.csv")

# Preview the data
print(df.shape)
print(df.head())

# Handle missing values
df['director'] = df['director'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Drop rows with essential null values
df = df.dropna(subset=['title'])

# Remove duplicates
df = df.drop_duplicates()

# Standardize text columns
df['type'] = df['type'].str.lower()
df['country'] = df['country'].str.title()
df['rating'] = df['rating'].str.upper().str.strip()

# Rename columns
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Fix data types
df['release_year'] = df['release_year'].astype(int)

# Save cleaned dataset
df.to_csv("cleaned_netflix.csv", index=False)
print("Cleaning complete. Cleaned data saved as cleaned_netflix.csv.")
