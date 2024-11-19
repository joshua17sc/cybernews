import openai

def generate_podcast_script(summaries):
    script = "Hello and welcome to the latest edition of the Cybersecurity News Podcast.\n\n"
    for summary in summaries:
        script += f"Today, we discuss: {summary['title']}\n{summary['summary']}\n\n"
    script += "Thanks for tuning in, and be sure to stay safe online."
    return script

if __name__ == "__main__":
    from summarizer import summarize_news
    from news_collector import fetch_news
    summaries = summarize_news(fetch_news())
    podcast_script = generate_podcast_script(summaries)
    print(podcast_script)
