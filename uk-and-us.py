#!/usr/bin/env python

"""
Counts the occurrences of words in their British and American spelling.
Specifically, given a word with the US "ze" suffix, also count occurrences of
words with the UK "se" suffix (e.g. treat realize and realise the same).

https://www.hackerrank.com/challenges/uk-and-us
"""

import re


def count_occurrences(lines, words):
    """Counts occurrences of words with US and UK spelling in given lines."""
    for word in words:
        pattern = get_pattern(word)
        count = sum(len(pattern.findall(line)) for line in lines)
        print(count)


def get_pattern(word):
    """Compiles a regex pattern that matches the US and UK word spelling."""
    regex = '{0}[sz]e'.format(word[:-2])
    pattern = re.compile(regex)
    return pattern


if __name__ == '__main__':
    line_count = int(input())
    lines = [input() for _ in range(line_count)]
    word_count = int(input())
    words = (input() for _ in range(word_count))
    count_occurrences(lines, words)
