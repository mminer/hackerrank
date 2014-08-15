#!/usr/bin/env python

"""
Counts the occurrences of words in lines of text.

https://www.hackerrank.com/challenges/find-a-word
"""

import re


def count_occurrences(lines, words):
    """Counts occurrences of words in given lines."""
    for word in words:
        pattern = get_pattern(word)
        count = sum(len(pattern.findall(line)) for line in lines)
        print(count)


def get_pattern(word):
    """Compiles a regex pattern that matches the given word."""
    # Ensure word isn't preceded or followed by other letters.
    regex = '(?<!\w){0}(?!\w)'.format(word)
    pattern = re.compile(regex)
    return pattern


if __name__ == '__main__':
    line_count = int(input())
    lines = [input() for _ in range(line_count)]
    word_count = int(input())
    words = (input() for _ in range(word_count))
    count_occurrences(lines, words)
