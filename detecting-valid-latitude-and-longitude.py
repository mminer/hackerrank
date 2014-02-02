#!/usr/bin/env python

"""
Given a line of text possibly containing latitude and longitude of a point, use
regular expressions to identify latitude and longitude referred to (if any).
"""

import re


def validate_pairs(pairs):
    """Prints 'Valid' for valid lat/lon pairs, 'Invalid' otherwise."""
    latlon_pattern = (
        '^\('  # Opening bracket
        '[-+]?'  # Sign (optional)
        '((([1-9]|[1-8]\d)(\.\d+)?)|90(\.0+)?)'  # 1 - 90
        ', '
        '[-+]?'  # Sign (optional)
        '((([1-9]|[1-9]\d|1[0-7]\d)(\.\d+)?)|180(\.0+)?)'  # 1 - 180
        '\)$'  # Closing bracket
    )

    pattern = re.compile(latlon_pattern)

    for pair in pairs:
        print('Valid' if pattern.match(pair) else 'Invalid')


if __name__ == '__main__':
    pair_count = int(input())
    pairs = [input() for _ in range(pair_count)]
    validate_pairs(pairs)
