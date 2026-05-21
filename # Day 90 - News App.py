# Day 90 - Final Project: News App 
import json
from urllib.request import urlopen
from urllib.error import URLError

def fetch_news():
    try:
        with urlopen("https://jsonplaceholder.typicode.com/posts") as response:
            data = json.loads(response.read().decode("utf-8"))
        return data[:5]
    except URLError:
        return [
            {"title": "Offline Mode", "body": "Could not fetch live news."},
            {"title": "Day 90", "body": "Python roadmap completed."}
        ]

articles = fetch_news()

print("=== Top News ===")
for i, article in enumerate(articles, 1):
    print(f"{i}. {article['title']}")
    print(article['body'])
    print()