from google_play_scraper import reviews, Sort
import pandas as pd
import os

# Define app IDs (replace with verified IDs)
apps = {
    'CBE': 'com.combanketh.mobilebanking',
    'BOA': 'com.boa.boaMobileBanking',
    'Dashen': 'com.dashen.dashensuperapp'
}

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Scrape reviews
all_reviews = []
for bank, app_id in apps.items():
    print(f"Scraping reviews for {bank}...")
    try:
        result, _ = reviews(
            app_id,
            lang='en',          # English reviews
            country='et',       # Ethiopia
            sort=Sort.NEWEST,   # Sort by newest
            count=400,          # Target 400 reviews per bank
            filter_score_with=None  # All ratings
        )
        for review in result:
            all_reviews.append({
                'review': review['content'],
                'rating': review['score'],
                'date': review['at'].strftime('%Y-%m-%d'),
                'bank': bank,
                'source': 'Google Play'
            })
    except Exception as e:
        print(f"Error scraping {bank}: {e}")

# Save to DataFrame and CSV
df = pd.DataFrame(all_reviews)
df.to_csv('data/raw_reviews.csv', index=False)
print(f"Saved {len(df)} reviews to data/raw_reviews.csv")