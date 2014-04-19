#!/usr/bin/env python

"""
Identifies whether a fictional identification number is valid.

https://www.hackerrank.com/challenges/utopian-identification-number
"""

import re


def validate_ids(ids):
    """Prints 'VALID' for valid IDs, 'INVALID' otherwise."""
    pattern = get_pattern()

    for citizen_id in ids:
        print('VALID' if pattern.match(citizen_id) else 'INVALID')


def get_pattern():
    """Compiles a regex pattern that matches the fictional ID format."""
    regex = '^[a-z]{,3}\d{2,8}[A-Z]{3,}$'
    pattern = re.compile(regex)
    return pattern


if __name__ == '__main__':
    id_count = int(input())
    ids = [input() for _ in range(id_count)]
    validate_ids(ids)
