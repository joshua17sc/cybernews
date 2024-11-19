# Cybersecurity Podcast Automation

This repository provides a fully automated solution for creating and publishing a cybersecurity news podcast. Using GitHub Actions, OpenAI, Google Cloud Text-to-Speech, Medium, and Podbean, this project automates the process of collecting news, summarizing it, creating a blog, generating a podcast script, recording audio, and publishing the content.

## Overview
The automation workflow includes:
1. **Collecting Cybersecurity News**: Fetching recent cybersecurity news articles using RSS feeds and web scraping.
2. **Summarizing News**: Using OpenAI's GPT-4 API to summarize the collected news articles.
3. **Creating a Blog Post**: Publishing a blog post to Medium summarizing the key news stories.
4. **Generating a Podcast Script**: Creating a podcast script using the summarized content.
5. **Recording the Podcast**: Using Google Cloud Text-to-Speech to record the podcast.
6. **Publishing the Podcast**: Uploading the recorded podcast to Podbean for distribution.

## Tools and Technologies Used
- **GitHub Actions**: For orchestrating the automation workflow.
- **Python**: Scripts are written in Python for collecting, summarizing, and processing content.
- **OpenAI GPT-4**: Summarizes news articles and generates the podcast script.
- **Google Cloud Text-to-Speech**: Converts the generated script into an audio recording.
- **Medium API**: Publishes summarized content as a blog post.
- **Podbean API**: Publishes the recorded podcast for distribution.

## Prerequisites
- **Python 3.8+** installed locally for development.
- **GitHub Account** with access to create and use GitHub Actions.
- **API Keys and Tokens**:
  - **OpenAI API Key**: For generating summaries and podcast scripts.
  - **Medium API Token**: For publishing blog posts.
  - **Google Cloud Credentials**: For Google Cloud Text-to-Speech.
  - **Podbean Access Token**: For uploading podcasts.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/cybersecurity-podcast-automation.git
   cd cybersecurity-podcast-automation
   ```

2. **Install Dependencies**:
   Install the required Python libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add Secrets to GitHub**:
   Add the following secrets to your GitHub repository for use with GitHub Actions:
   - `OPENAI_API_KEY`: Your OpenAI API key.
   - `MEDIUM_API_TOKEN`: Your Medium API token.
   - `GOOGLE_CREDENTIALS`: Your Google Cloud credentials JSON.
   - `PODBEAN_ACCESS_TOKEN`: Your Podbean access token.

4. **Configure Google Cloud**:
   - Create a service account in Google Cloud and download the JSON key.
   - Add the path to the credentials file as an environment variable (`GOOGLE_APPLICATION_CREDENTIALS`).

5. **Run Locally (Optional)**:
   To run the workflow locally, execute the Python scripts in the following order:
   ```bash
   python news_collector.py
   python summarizer.py
   python medium_post_creator.py
   python podcast_script_generator.py
   python podcast_recorder.py
   python podcast_uploader.py
   ```

## GitHub Actions Workflow
The GitHub Actions workflow (`.github/workflows/automation.yml`) is set to run daily at 7 AM UTC. It performs the following steps:
1. Collect news articles.
2. Summarize the collected news.
3. Create a Medium blog post.
4. Generate a podcast script and record the podcast.
5. Upload the podcast to Podbean.

## Repository Structure
- **news_collector.py**: Collects the latest cybersecurity news from RSS feeds.
- **summarizer.py**: Summarizes the collected news using OpenAI's API.
- **medium_post_creator.py**: Publishes a blog post to Medium.
- **podcast_script_generator.py**: Generates a script for the podcast.
- **podcast_recorder.py**: Records the podcast using Google Cloud TTS.
- **podcast_uploader.py**: Uploads the podcast to Podbean.
- **.github/workflows/automation.yml**: Defines the GitHub Actions workflow for automation.

## Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly appreciated.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
For questions or support, please reach out to [your-email@example.com].

## Future Enhancements
- Add more advanced filtering to the news collection process.
- Improve the podcast's audio quality using post-processing tools.
- Introduce sentiment analysis to better understand the tone of news articles.

---
Feel free to customize and enhance this project as you see fit!

