**Reddit Scraper + Gemini AI Summary**

A Python program that scrapes Reddit posts for a specified subreddit and search term, then uses Google's Gemini AI to create a summary. Has a basic Tkinter GUI for intuitive user interaction.

**Features**


Search any subReddit for posts matching a query

Get up to 20 post titles and text

Use Gemini AI to create a summary paragraph based on those posts

Intuitive Tkinter interface for input and output

**Setup**

Clone the repo

git clone [https://github.com/yourusername/yourrepo.git](https://github.com/zacharyburricepython/reddit-scraper-ai)

cd reddit-scraper-ai

Create a .env file at the root of the project with your API keys:

REDDIT_CLIENT_ID=your_reddit_client_id

REDDIT_CLIENT_SECRET=your_reddit_client_secret

REDDIT_USER_AGENT=your_user_agent

GENAI_API_KEY=your_gemini_api_key

**Install requirements**

pip install -r requirements.txt

**Usage**


Run the script:

python main.py

Enter the subreddit name (no r/) and your search query, then click Fetch and Summarize.

**Notes:**


Make sure your .env file is not committed to GitHub so your API keys are not shared.

The app utilizes internet connection for API requests.

tkinter comes pre-installed with Python, so don't include it in requirements.txt.




License
MIT License © Zachary Burrice
