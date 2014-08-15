#!/usr/bin/env python

"""
Determines how many tweets contain the string 'hackerrank'.

https://www.hackerrank.com/challenges/hackerrank-tweets
"""

import re


def count_mentions(tweets, keyword):
    """Counts the number of tweets that contain the given keyword."""
    pattern = re.compile('^.*hackerrank.*$', re.IGNORECASE)
    matching_tweets = [tweet for tweet in tweets if pattern.match(tweet)]
    count = len(matching_tweets)
    return count


if __name__ == '__main__':
    tweet_count = int(input())
    tweets = (input() for _ in range(tweet_count))
    print(count_mentions(tweets, 'hackerrank'))
