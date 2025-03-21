import requests
from bs4 import BeautifulSoup
import re

def fetch_news(company_name):
    search_url = f"https://news.google.com/search?q={company_name}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article")[:10]  # Limit to 10 articles
    news_list = []

    for article in articles:
        title_tag = article.find("h3")
        if title_tag:
            title = title_tag.get_text()
            link = "https://news.google.com" + title_tag.a["href"][1:]

            news_list.append({"title": title, "link": link})

    return news_list

if __name__ == "__main__":
    company = "Tesla"
    news = fetch_news(company)
    print(news)
    