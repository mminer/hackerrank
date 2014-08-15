#!/usr/bin/env python

"""
Finds the only number in a list of numbers that isn't a pair.
To do this efficiently we use the property that x ^ x = 0. XORing all numbers
cancels out identical numbers and leaves us with the one we're after.

https://www.hackerrank.com/challenges/lonely-integer
"""

from functools import reduce


def find_lonely_integer(numbers):
    """Finds the number that has no twin."""
    lonely_integer = reduce(lambda x, y: x ^ y, numbers)
    return lonely_integer


if __name__ == '__main__':
    number_count = int(input())
    numbers = (int(x) for x in input().split())
    print(find_lonely_integer(numbers))
