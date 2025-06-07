import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/reviews_with_sentiment.csv')

# Rating distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='rating', hue='bank')
plt.title('Rating Distribution by Bank')
plt.xlabel('Rating (1-5 Stars)')
plt.ylabel('Number of Reviews')
plt.savefig('visualizations/rating_distribution.png')
plt.close()