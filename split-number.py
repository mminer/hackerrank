#!/usr/bin/env python

"""
Splits phone numbers into their country code, local area code, and number.

https://www.hackerrank.com/challenges/split-number
"""

import re


def split_phone_numbers(numbers):
    """Prints the separated groups of phone numbers."""
    pattern = get_pattern()

    for number in numbers:
        match = pattern.match(number)
        output = ('CountryCode={country_code},'
                  'LocalAreaCode={area_code},'
                  'Number={number}').format(**match.groupdict())
        print(output)


def get_pattern():
    """Compiles a regex pattern that groups phone number parts."""
    regex = (
        '(?P<country_code>\d{1,3})'
        '[ -]'
        '(?P<area_code>\d{1,3})'
        '[ -]'
        '(?P<number>\d{4,10})'
    )

    pattern = re.compile(regex)
    return pattern


if __name__ == '__main__':
    number_count = int(input())
    numbers = (input() for _ in range(number_count))
    split_phone_numbers(numbers)
