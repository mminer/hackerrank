#!/usr/bin/env python

"""
Counts the number of square integers (inclusive) between two given numbers.

https://www.hackerrank.com/challenges/sherlock-and-squares
"""

import math


def squares_between(a, b):
    """Finds the number of square integers between a and b."""
    count = math.floor(math.sqrt(b)) - math.floor(math.sqrt(a - 1))
    return count


if __name__ == '__main__':
    test_count = int(input())

    for _ in range(test_count):
        a, b = tuple(int(pair) for pair in input().split())
        print(squares_between(a, b))
