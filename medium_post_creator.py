import requests
import os

def create_medium_post(summaries):
    token = os.getenv('MEDIUM_API_TOKEN')
    user_url = "https://api.medium.com/v1/me"
    headers = {"Authorization": f"Bearer {token}"}
    
    user_response = requests.get(user_url, headers=headers)
    user_id = user_response.json()["data"]["id"]
    
    post_url = f"https://api.medium.com/v1/users/{user_id}/posts"
    
    content = ""
    for summary in summaries:
        content += f"<h2>{summary['title']}</h2><p>{summary['summary']}</p><a href='{summary['url']}'>Read more here</a><br><br>"
    
    post_data = {
        "title": "Weekly Cybersecurity News Summary",
        "contentFormat": "html",
        "content": content,
        "publishStatus": "public"
    }
    
    response = requests.post(post_url, headers=headers, json=post_data)
    if response.status_code == 201:
        print("Blog post created successfully.")
    else:
        print("Failed to create blog post:", response.text)

if __name__ == "__main__":
    from summarizer import summarize_news
    from news_collector import fetch_news
    summaries = summarize_news(fetch_news())
    create_medium_post(summaries)
