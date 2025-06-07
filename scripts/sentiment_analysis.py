import pandas as pd
from transformers import pipeline
import uuid

# Load cleaned data
df = pd.read_csv('data/cleaned_reviews.csv')

# Initialize sentiment classifier
classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

# Add review_id
df['review_id'] = [str(uuid.uuid4()) for _ in range(len(df))]

# Compute sentiment
def get_sentiment(text):
    try:
        # Truncate to 512 tokens (DistilBERT's max length)
        result = classifier(text[:512])[0]
        label = 'NEUTRAL' if result['label'] == 'POSITIVE' and result['score'] < 0.6 else result['label']
        return label, result['score']
    except Exception as e:
        print(f"Error processing review: {e}")
        return 'NEUTRAL', 0.0

# Apply sentiment analysis
df[['sentiment_label', 'sentiment_score']] = df['review'].apply(get_sentiment).apply(pd.Series)

# Save results
df.to_csv('data/reviews_with_sentiment.csv', index=False)
print(f"Saved {len(df)} reviews with sentiment to data/reviews_with_sentiment.csv")

# Aggregate sentiment by bank and rating
sentiment_summary = df.groupby(['bank', 'rating', 'sentiment_label']).size().unstack(fill_value=0)
print("\nSentiment Summary by Bank and Rating:")
print(sentiment_summary)

# Check KPI: Sentiment scores for 90%+ reviews
scored_reviews = len(df[df['sentiment_score'] > 0.0])
print(f"Scored {scored_reviews} reviews ({(scored_reviews / len(df)) * 100:.2f}% of total)")