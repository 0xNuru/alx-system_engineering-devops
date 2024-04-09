#!/usr/bin/python3
"""
a script that queries the Reddit API and
returns the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """return 10 hottest posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "RedditSubscribersCountBot/0.1 by nurvdeen"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(None)

    try:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    except ValueError:
        print(None)
