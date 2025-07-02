import praw
import google.generativeai as genai
import tkinter as tk
import prawcore
from dotenv import load_dotenv
import os

load_dotenv()


# PRAW setup
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_USER_AGENT')
)

# Gemini setup
genai.configure(api_key=os.getenv('GENAI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

# Tkinter window
window = tk.Tk()
window.title("Reddit Scraper with Gemini")
window.geometry("800x600")

# Labels
tk.Label(window, text="Subreddit (do not include 'r/':").pack()
sub_entry = tk.Entry(window)
sub_entry.pack()

tk.Label(window, text="Search Query:").pack()
query_entry = tk.Entry(window)
query_entry.pack()

output_box = tk.Text(window, wrap='word')
output_box.pack(expand=True, fill='both', padx=10, pady=10)

def fetch_and_summarize():
    sub = sub_entry.get().strip()
    query = query_entry.get().strip()

    all_posts = ""
    try:
        for post in reddit.subreddit(sub).search(query, limit=20, sort='year', time_filter='all'):
            post_title = post.title
            post_text = post.selftext
            
            
            all_posts += "__________New post________"
            all_posts += f"Title: {post_title}"
            all_posts += f"Text: {post_text}"
    except prawcore.exceptions.Redirect:
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, 'Error: Subreddit does not exist')
        return




    prompt = (
        f'Summarize the info you get from these reddit posts. The topic that should be discussed is about {query}, '
        f'so use the posts to find info about that. If the topic is very broad, then talk about multiple things within '
        f'that topic. If it is specific then use info specific to the topic. Create a short essay/paragraph (keep it '
        f'fairly short but still good info) that uses information for that topic. Attempt to only use info from posts '
        f'that give real data surronding the topic. Attempt to reference posts made within the summary. Use the given '
        f'top comments of the posts to use for answering questions or extra info. You are a reddit data scraper bot. '
        f' PS: If you do not receive any reddit posts, then please say "Error, you may not have correctly entered a search query": \n\n' 
        + all_posts
    )

    response = model.generate_content(prompt)

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, response.text)

# Button
tk.Button(window, text="Fetch and Summarize", command=fetch_and_summarize).pack(pady=10)

window.mainloop()


