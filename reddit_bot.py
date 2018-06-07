import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')


subreddit = reddit.subreddit('soccer')
for submission in subreddit.hot(limit=200):
        if re.search("sporting", submission.title, re.IGNORECASE):
            print("Bot found : ", submission.title)
        
