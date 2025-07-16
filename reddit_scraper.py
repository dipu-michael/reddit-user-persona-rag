import praw
import os
import json
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def scrape_user(username, max_items=50):
    user = reddit.redditor(username)
    data = []

    for comment in user.comments.new(limit=max_items):
        data.append({
            "type": "comment",
            "text": comment.body,
            "url": f"https://reddit.com{comment.permalink}"
        })

    for submission in user.submissions.new(limit=max_items):
        data.append({
            "type": "post",
            "text": submission.title + "\n" + submission.selftext,
            "url": f"https://reddit.com{submission.permalink}"
        })

    os.makedirs("data", exist_ok=True)
    with open(f"data/{username}.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Scraped and saved {len(data)} items to data/{username}.json")

# For test run:
if __name__ == "__main__":
    scrape_user("kojied")
