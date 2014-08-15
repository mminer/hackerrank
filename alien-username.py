#!/usr/bin/env python

"""
Identifies whether fictional alien usernames are valid.

https://www.hackerrank.com/challenges/alien-username
"""

import re


def validate_usernames(usernames):
    """Prints 'VALID' for valid usernames, 'INVALID' otherwise."""
    pattern = re.compile('^[_\.]\d+[a-z]*_?$', re.IGNORECASE)

    for username in usernames:
        print('VALID' if pattern.match(username) else 'INVALID')


if __name__ == '__main__':
    username_count = int(input())
    usernames = (input() for _ in range(username_count))
    validate_usernames(usernames)
