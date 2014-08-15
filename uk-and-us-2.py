#!/usr/bin/env python

"""
Counts the occurrences of words in their British and American spelling.
Specifically, given a word containing the UK "our", also count occurences of
words with the US "or" (e.g. treat colour and color the same).

https://www.hackerrank.com/challenges/uk-and-us-2
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
    word_regex = word.replace('our', 'ou?r')
    # Ensure word isn't substring of another / followed by other letters.
    # That is, we don't want a match for "savour" with the word "savoury".
    regex = '{0}(?!\w)'.format(word_regex)
    pattern = re.compile(regex)
    return pattern


if __name__ == '__main__':
    line_count = int(input())
    lines = [input() for _ in range(line_count)]
    word_count = int(input())
    words = (input() for _ in range(word_count))
    count_occurrences(lines, words)
