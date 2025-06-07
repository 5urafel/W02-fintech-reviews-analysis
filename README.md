# Fintech Reviews Analysis

## 10 Academy Artificial Intelligence Mastery - Week 2 Challenge

### Overview

This project analyzes customer reviews from the Google Play Store for three Ethiopian banks (CBE, BOA, Dashen) to improve mobile app user experience. Tasks include web scraping, sentiment and thematic analysis, Oracle database storage, and visualization of insights.

### Setup Instructions

1. Clone the repository: `git clone git@github.com:5urafel/W02-fintech-reviews-analysis.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Install spaCy model: `python -m spacy download en_core_web_sm`

### Methodology

(To be updated as tasks progress)

- Task 1: Scrape 1,200+ reviews using `google-play-scraper`.
- Task 2: Perform sentiment and thematic analysis using DistilBERT and spaCy.
- Task 3: Store data in Oracle XE database.
- Task 4: Visualize insights and provide recommendations.

### Directory Structure

- `data/`: Stores raw and cleaned datasets (not committed).
- `scripts/`: Python scripts for scraping, preprocessing, analysis, and database operations.
- `visualizations/`: Output plots and word clouds.
- `tests/`: Unit tests for scripts.
