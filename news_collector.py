import feedparser
from newspaper import Article

def fetch_news():
    feeds = [
        "https://thehackernews.com/feeds/posts/default",
        "https://krebsonsecurity.com/feed/",
    ]
    news_list = []

    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            try:
                article = Article(entry.link)
                article.download()
                article.parse()
                news_list.append({
                    "title": entry.title,
                    "summary": article.summary,
                    "content": article.text,
                    "url": entry.link
                })
            except:
                continue
    return news_list

if __name__ == "__main__":
    latest_news = fetch_news()
    for news in latest_news:
        print(news["title"])
