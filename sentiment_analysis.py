import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Download NLTK data
nltk.download("punkt")

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    if scores["compound"] >= 0.05:
        return "Positive"
    elif scores["compound"] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    text = "Tesla is making huge advancements in electric vehicles."
    print(analyze_sentiment(text))
