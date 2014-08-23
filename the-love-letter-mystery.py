#!/usr/bin/env python

"""
Counts the number of operations required to convert a word to a palindrome.

https://www.hackerrank.com/challenges/the-love-letter-mystery
"""

from itertools import islice


def count_operations(word):
    """Determines operations needed to convert word -> palindrome."""
    difference = lambda x, y: abs(ord(x) - ord(y))
    median = len(word) // 2
    pairs = zip(word, reversed(word))
    operations = sum(difference(x, y) for x, y in islice(pairs, median))
    return operations


if __name__ == '__main__':
    word_count = int(input())

    for _ in range(word_count):
        word = input()
        print(count_operations(word))
