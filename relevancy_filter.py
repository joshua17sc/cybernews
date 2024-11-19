import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # Get API key from environment variable
)

def filter_top_articles(articles):
    # Create messages to pass to the model for scoring
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that selects the most relevant cybersecurity news articles based on their content."
        }
    ]

    for i, article in enumerate(articles):
        messages.append(
            {
                "role": "user",
                "content": f"Article {i + 1}:\nTitle: {article['title']}\nSummary: {article['summary']}\n"
            }
        )

    messages.append(
        {
            "role": "user",
            "content": "Please provide a score for each article from 1 to 10 based on how relevant it is to current cybersecurity trends. Provide the scores in the format: 'Article X: Score'."
        }
    )

    # Make the request to create the chat completion
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
    )

    # Extract the response text
    scores_text = response['choices'][0]['message']['content'].strip().split("\n")
    scores = {}

    # Process the response to extract scores
    for line in scores_text:
        parts = line.split(":")
        if len(parts) == 2:
            article_index = int(parts[0].split()[-1]) - 1
            score = int(parts[1].strip())
            scores[article_index] = score

    # Sort the articles based on the scores and select the top 8
    sorted_articles = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_articles = [articles[i] for i, _ in sorted_articles[:8]]

    return top_articles

if __name__ == "__main__":
    from news_collector import fetch_news
    news_list = fetch_news()
    top_articles = filter_top_articles(news_list)
    for article in top_articles:
        print(article["title"])
