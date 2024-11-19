import requests
import os

def upload_podcast(file_path):
    access_token = os.getenv('PODBEAN_ACCESS_TOKEN')
    url = "https://api.podbean.com/v1/files/upload"

    files = {"file": open(file_path, "rb")}
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        print("Podcast uploaded successfully.")
    else:
        print("Failed to upload podcast:", response.text)

if __name__ == "__main__":
    upload_podcast("cyber_news_podcast.mp3")
