#!/usr/bin/env python

"""
Determines whether a string can be rearranged to form a palindrome.

https://www.hackerrank.com/challenges/game-of-thrones
"""

from collections import Counter


def can_be_palindrome(string):
    """Returns true if a string is an anagram of a palindrome."""
    # Observation: one letter can appear odd number of times in a palindrome.
    # The rest must appear an even number of times.
    letter_counts = Counter(string).values()
    odd_counts = [count for count in letter_counts if count % 2 != 0]
    return len(odd_counts) <= 1


if __name__ == '__main__':
    string = input()
    print('YES' if can_be_palindrome(string) else 'NO')
