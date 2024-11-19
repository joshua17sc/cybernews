import os
import anthropic

# Set your Claude API key
claude_api_key = os.getenv("CLAUDE_API_KEY")
client = anthropic.Anthropic(api_key=claude_api_key)

def filter_top_articles(articles):
    # Construct the prompt for Claude
    prompt = "You are an AI assistant tasked with ranking cybersecurity news articles. Rate each article based on its relevance to current cybersecurity trends, from 1 to 10.\n\n"

    for i, article in enumerate(articles):
        prompt += f"Article {i + 1}:\nTitle: {article['title']}\nSummary: {article['summary']}\n\n"

    prompt += "Please provide a score for each article in the format: 'Article X: Score'."

    # Send the request to Claude for completion
    response = client.completions.create(
        model="claude-2",
        prompt=prompt,
        max_tokens_to_sample=150,
        temperature=0.7,
    )

    # Extract the response text
    scores_text = response["completion"].strip().split("\n")
    scores = {}

    # Parse the response to extract scores
    for line in scores_text:
        parts = line.split(":")
        if len(parts) == 2:
            article_index = int(parts[0].split()[-1]) - 1
            score = int(parts[1].strip())
            scores[article_index] = score

    # Sort the articles based on scores and select the top 8
    sorted_articles = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_articles = [articles[i] for i, _ in sorted_articles[:8]]

    return top_articles

if __name__ == "__main__":
    from news_collector import fetch_news
    news_list = fetch_news()
    top_articles = filter_top_articles(news_list)
    for article in top_articles:
        print(article["title"])
