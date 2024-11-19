from google.cloud import texttospeech
import os

def record_podcast(script, filename="cyber_news_podcast.mp3"):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=script)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    
    response = client.synthesize_speech(
        input=input_text,
        voice=voice,
        audio_config=audio_config
    )
    
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f"Podcast audio saved to {filename}")

if __name__ == "__main__":
    from podcast_script_generator import generate_podcast_script
    from summarizer import summarize_news
    from news_collector import fetch_news
    summaries = summarize_news(fetch_news())
    podcast_script = generate_podcast_script(summaries)
    record_podcast(podcast_script)
