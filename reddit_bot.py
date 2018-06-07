import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')

title = input("Enter your topic to search: ")
subreddit = input("Enter your subreddit of interest: ")
limit = int (input("Enter the limit of search in hot: "))
subreddit = reddit.subreddit(subreddit)
for submission in subreddit.hot(limit=limit):
        if re.search(title, submission.title, re.IGNORECASE):
            print("Bot found this post: ", submission.title)
        
