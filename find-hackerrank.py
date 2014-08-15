#!/usr/bin/env python

"""
Given a list of conversations, figures out which ones:

- Start with "hackerrank"
- End with "hackerrank"
- Start and end with "hackerrank"

https://www.hackerrank.com/challenges/find-hackerrank
"""

import re


def find_conversation_ranks(conversations):
    """Prints numeric ranks of conversations."""
    # Compile regex patterns.
    start_pattern = re.compile('^hackerrank')
    end_pattern = re.compile('hackerrank$')
    start_and_end_pattern = re.compile('^hackerrank$')

    for conversation in conversations:
        if start_and_end_pattern.match(conversation):
            print(0)
        elif start_pattern.match(conversation):
            print(1)
        elif end_pattern.match(conversation):
            print(2)
        else:
            print(-1)


if __name__ == '__main__':
    conversation_count = int(input())
    conversations = (input() for _ in range(conversation_count))
    find_conversation_ranks(conversations)
