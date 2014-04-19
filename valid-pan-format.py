#!/usr/bin/env python

"""
Identifies whether PAN numbers are valid.

https://www.hackerrank.com/challenges/valid-pan-format
"""

import re


def validate_pan_numbers(numbers):
    """Prints 'YES' for valid IDs, 'NO' otherwise."""
    pattern = get_pattern()

    for number in numbers:
        print('YES' if pattern.match(number) else 'NO')


def get_pattern():
    """Compiles a regex pattern that matches the PAN number format."""
    regex = '^[A-Z]{5}\d{4}[A-Z]$'
    pattern = re.compile(regex)
    return pattern


if __name__ == '__main__':
    number_count = int(input())
    numbers = [input() for _ in range(number_count)]
    validate_pan_numbers(numbers)
