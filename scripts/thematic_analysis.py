import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import re

# Load data
df = pd.read_csv('data/reviews_with_sentiment.csv')

# Initialize spaCy
nlp = spacy.load('en_core_web_sm')

# Extract keywords
def extract_keywords(text):
    doc = nlp(text.lower())
    # Keep nouns, adjectives, and verbs, exclude stop words
    tokens = [token.lemma_ for token in doc if token.pos_ in ['NOUN', 'ADJ', 'VERB'] and not token.is_stop]
    return tokens

df['keywords'] = df['review'].apply(extract_keywords)

# TF-IDF for n-grams (to identify phrases like "login error")
vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english', max_features=50)
tfidf_matrix = vectorizer.fit_transform(df['review'])
feature_names = vectorizer.get_feature_names_out()

# Print top TF-IDF terms for reference
print("Top TF-IDF Terms:", feature_names[:10])

# Define themes and associated keywords
themes = {
    'Account Access Issues': ['login', 'authentication', 'password', 'access', 'sign in'],
    'Transaction Performance': ['transfer', 'slow', 'loading', 'timeout', 'transaction'],
    'User Interface': ['ui', 'interface', 'design', 'navigation', 'layout'],
    'Customer Support': ['support', 'response', 'help', 'customer', 'service'],
    'Feature Requests': ['fingerprint', 'budget', 'feature', 'option', 'add']
}

# Assign themes to reviews
def assign_themes(keywords):
    assigned = []
    for theme, theme_keywords in themes.items():
        if any(re.search(r'\b' + re.escape(kw) + r'\b', ' '.join(keywords)) for kw in theme_keywords):
            assigned.append(theme)
    return assigned if assigned else ['Other']

df['themes'] = df['keywords'].apply(assign_themes)

# Save results
df.to_csv('data/reviews_with_themes.csv', index=False)
print(f"Saved {len(df)} reviews with themes to data/reviews_with_themes.csv")

# Summarize themes by bank
theme_summary = df.explode('themes').groupby(['bank', 'themes']).size().unstack(fill_value=0)
print("\nTheme Summary by Bank:")
print(theme_summary)