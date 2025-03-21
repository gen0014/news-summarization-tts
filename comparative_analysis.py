import pandas as pd
from collections import Counter

def compare_sentiments(news_list):
    sentiment_counts = Counter([article["sentiment"] for article in news_list])

    return {
        "Sentiment Distribution": sentiment_counts,
        "Insights": [
            f"News coverage is mostly {max(sentiment_counts, key=sentiment_counts.get)}"
        ],
    }

if __name__ == "__main__":
    sample_articles = [
        {"title": "Tesla's stock rises", "sentiment": "Positive"},
        {"title": "Tesla faces legal issues", "sentiment": "Negative"},
    ]
    print(compare_sentiments(sample_articles))
