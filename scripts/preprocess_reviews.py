import pandas as pd

# Load raw data
df = pd.read_csv('data/raw_reviews.csv')

# Remove duplicates
initial_count = len(df)
df = df.drop_duplicates(subset=['review', 'bank'])
print(f"Removed {initial_count - len(df)} duplicates")

# Handle missing data
df = df.dropna(subset=['review', 'rating'])
missing_data = df.isnull().sum()
print(f"Missing data: {missing_data}")

# Normalize dates
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

# Basic text cleaning (optional: remove extra spaces, special characters)
df['review'] = df['review'].str.strip().replace(r'\s+', ' ', regex=True)

# Ensure rating is between 1 and 5
df = df[df['rating'].isin([1, 2, 3, 4, 5])]

# Save cleaned data
df.to_csv('data/cleaned_reviews.csv', index=False)
print(f"Saved {len(df)} cleaned reviews to data/cleaned_reviews.csv")

# Verify data quality
print(f"Data quality check: {len(df)} reviews, <5% missing: {(missing_data.sum() / initial_count) * 100:.2f}%")