#!/usr/bin/python3
"""a script that queries the Reddit API and return the number of subs"""
import requests

def number_of_subscribers(subreddit):
    """print number of subscribers to a subreddit"""
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    userAgent = "Mozilla/5.0"

    response = requests.get(url, headers={"user-agent": userAgent})
    if not response:
        return 0
    retValue = response.json().get('data').get('subscribers')
    if retValue:
        return retValue
    else:
        return 0
