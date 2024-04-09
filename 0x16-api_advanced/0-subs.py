#!/usr/bin/python3
"""a script that queries the Reddit API and returns the number of subscribers"""
import requests



def number_of_subscribers(subreddit):
    """print number of subscribers to a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "RedditSubscribersCountBot/0.1 by nurvdeen"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    
    try:
        data = response.json()
        if "data" in data and "subscribers" in data["data"]:
            return data["data"]["subscribers"]
        else:
            return 0
    except ValueError:
        # In case the response isn't a valid JSON
        return 0

