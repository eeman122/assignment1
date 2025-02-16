import praw
import csv
import os 
import json

import pandas as pd
from pytrends.request import TrendReq

reddit = praw.Reddit(
    client_id="YCIS-wDpZ271OI3ZU6kzRg",
    client_secret="gKiwpWUOVcZEno2lmtqyLBafFzX-BA",
    user_agent="EVDataCollector v1.0"
)

def fetch_reddit_posts(keyword, limit=200):
    posts = []
    for submission in reddit.subreddit("all").search(keyword, limit=limit):
        posts.append([
            submission.title,
            submission.selftext,
            submission.author.name if submission.author else "[deleted]",
            submission.created_utc,
            submission.score,
            submission.subreddit.display_name
        ])
    return posts

def save_to_csv(data, filename="reddit_posts.csv"):
    headers = ["Title", "Post Text", "Author", "Date", "Upvotes", "Subreddit"]
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
    print(f"Data saved to {filename}")
    
if __name__ == "__main__":
    keyword = ["electric vehicle", "tesla", "ev charging"]
    posts_data = fetch_reddit_posts(keyword, limit=100)
    save_to_csv(posts_data)
    
reddit_df = pd.read_csv("reddit_posts.csv")
print(reddit_df.describe())
# print(reddit_df)