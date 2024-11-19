import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def filter_top_articles(articles):
    # Create the conversation messages to pass to the model
    messages = [
        {"role": "system", "content": "You are a helpful assistant that selects the most relevant cybersecurity news articles based on their content."}
    ]

    # Add each article as a separate message
    for i, article in enumerate(articles):
        messages.append(
            {"role": "user", "content": f"Article {i+1}:\nTitle: {article['title']}\nSummary: {article['summary']}\n"}
        )

    # Add the final request for scoring
    messages.append({"role": "user", "content": "Please provide a score for each article from 1 to 10 based on how relevant it is to current cybersecurity trends. Provide the scores in the format: 'Article X: Score'."})

    # Request a response from the model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150,
        temperature=0.7
    )

    # Extract scores from the response
    scores_text = response['choices'][0]['message']['content'].strip().split("\n")
    scores = {}

    for line in scores_text:
        parts = line.split(":")
        if len(parts) == 2:
            article_index = int(parts[0].split()[-1]) - 1
            score = int(parts[1].strip())
            scores[article_index] = score

    # Sort articles based on their scores
    sorted_articles = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_articles = [articles[i] for i, _ in sorted_articles[:8]]

    return top_articles

if __name__ == "__main__":
    from news_collector import fetch_news
    news_list = fetch_news()
    top_articles = filter_top_articles(news_list)
    for article in top_articles:
        print(article["title"])
