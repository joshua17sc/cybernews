import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def summarize_news(news):
    summaries = []
    for item in news:
        try:
            response = openai.Completion.create(
                engine="gpt-4",
                prompt=f"Summarize the following cybersecurity news in a concise and engaging way:\n\n{item['content']}",
                max_tokens=150
            )
            summaries.append({
                "title": item['title'],
                "summary": response.choices[0].text.strip(),
                "url": item['url']
            })
        except Exception as e:
            print(f"Error: {e}")
            continue
    return summaries

if __name__ == "__main__":
    from news_collector import fetch_news
    news_list = fetch_news()
    summarized_news = summarize_news(news_list)
    for summary in summarized_news:
        print(summary["title"], summary["summary"])
