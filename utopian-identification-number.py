#!/usr/bin/env python

"""
Identifies whether fictional identification numbers are valid.

https://www.hackerrank.com/challenges/utopian-identification-number
"""

import re


def validate_ids(ids):
    """Prints 'VALID' for valid IDs, 'INVALID' otherwise."""
    pattern = re.compile('^[a-z]{,3}\d{2,8}[A-Z]{3,}$')

    for citizen_id in ids:
        print('VALID' if pattern.match(citizen_id) else 'INVALID')


if __name__ == '__main__':
    id_count = int(input())
    ids = (input() for _ in range(id_count))
    validate_ids(ids)
