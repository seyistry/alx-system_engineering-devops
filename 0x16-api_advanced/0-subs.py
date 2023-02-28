#!/usr/bin/python3
"""
number of subs
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(url,
                       headers={'User-Agent':
                                'API (by u/seyistry)'}).json()
    subs = req.get("data", {}).get("subscribers", 0)
    return subs
