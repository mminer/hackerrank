#!/usr/bin/env python

"""
Detects if lines of text represent an IPv4 address, IPv6 address, or neither.

https://www.hackerrank.com/challenges/ip-address-validation
"""

import re


def validate_addresses(addresses):
    """Identifies the type of IP addresses (IPv4, IPv6, or "Neither")."""
    ipv4_pattern = get_ipv4_pattern()
    ipv6_pattern = get_ipv6_pattern()

    for address in addresses:
        if ipv4_pattern.match(address):
            print('IPv4')
        elif ipv6_pattern.match(address):
            print('IPv6')
        else:
            print('Neither')


def get_ipv4_pattern():
    """Compiles a regex pattern that matches IPv4 addresses."""
    byte = '([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])'  # 0 - 255
    regex = '^{0}(\.{0}){{3}}$'.format(byte)
    pattern = re.compile(regex)
    return pattern


def get_ipv6_pattern():
    """Compiles a regex pattern that matches IPv6 addresses."""
    hex_group = '[0-9A-Fa-f]{1,4}'  # Four hex digits
    regex = '^({0})(:{0}){{7}}$'.format(hex_group)
    pattern = re.compile(regex)
    return pattern


if __name__ == '__main__':
    address_count = int(input())
    addresses = (input() for _ in range(address_count))
    validate_addresses(addresses)
