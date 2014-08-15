#!/usr/bin/env python

"""
Determines which lines match the pattern 'hi<BLANK>' and aren't immediately
followed by the letter D. Both 'hi' and D are case-insensitive.

https://www.hackerrank.com/challenges/saying-hi
"""

import re


def print_valid_lines(lines):
    """Prints lines that meet the constraints."""
    pattern = re.compile('^hi [^d].*$', re.IGNORECASE)

    for line in lines:
        if pattern.match(line):
            print(line)


if __name__ == '__main__':
    line_count = int(input())
    lines = (input() for _ in range(line_count))
    print_valid_lines(lines)
