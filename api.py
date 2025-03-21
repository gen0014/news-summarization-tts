from fastapi import FastAPI
from news_scraper import fetch_news
from sentiment_analysis import analyze_sentiment
from comparative_analysis import compare_sentiments
from tts_hindi import generate_hindi_audio

app = FastAPI()

@app.get("/news/{company}")
def get_news(company: str):
    articles = fetch_news(company)
    for article in articles:
        article["sentiment"] = analyze_sentiment(article["title"])
    sentiment_report = compare_sentiments(articles)
    return {"company": company, "articles": articles, "sentiment_report": sentiment_report}

@app.get("/tts/")
def get_tts(text: str):
    output_file = generate_hindi_audio(text)
    return {"message": "Audio generated", "file": output_file}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
