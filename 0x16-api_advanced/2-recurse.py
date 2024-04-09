#!/usr/bin/python3
"""a script that performs recursive calls to an api"""
import requests


def recurse(subreddit, after=None, hot_list=None):
    """returns a list containing all hot articles for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "RedditshotlisttBot/0.1 by nurvdeen"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    if hot_list is None:
        hot_list = []

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None

    data = response.json()
    posts = data["data"]["children"]
    hot_list.extend(post["data"]["title"] for post in posts)
    after = data["data"]["after"]
    if after:
        return recurse(subreddit, after, hot_list)
    else:
        return hot_list
