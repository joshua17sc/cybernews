import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def filter_top_articles(articles):
    prompt = "You are a helpful assistant that selects the most relevant cybersecurity news articles. Here is a list of articles. For each article, provide a score from 1 to 10 based on how relevant it is to current cybersecurity trends:\n\n"
    for i, article in enumerate(articles):
        prompt += f"{i+1}. Title: {article['title']}\nSummary: {article['summary']}\n\n"

    prompt += "Please provide the score for each article in the format: 'Article X: Score'."

    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=150
    )
    
    scores_text = response.choices[0].text.strip().split("\n")
    scores = {}
    
    for line in scores_text:
        parts = line.split(":")
        if len(parts) == 2:
            article_index = int(parts[0].split()[-1]) - 1
            score = int(parts[1].strip())
            scores[article_index] = score

    sorted_articles = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_articles = [articles[i] for i, _ in sorted_articles[:8]]
    
    return top_articles

if __name__ == "__main__":
    from news_collector import fetch_news
    news_list = fetch_news()
    top_articles = filter_top_articles(news_list)
    for article in top_articles:
        print(article["title"])
