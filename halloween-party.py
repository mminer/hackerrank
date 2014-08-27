#!/usr/bin/env python

"""
Counts the number of times a piece of chocolate can be cut into 1x1 pieces.

https://www.hackerrank.com/challenges/halloween-party
"""


def count_pieces(k):
    """Calculates the number of 1x1 pieces that k cuts creates."""
    horizontal_cuts = k // 2
    vertical_cuts = k - horizontal_cuts
    pieces = horizontal_cuts * vertical_cuts
    return pieces


if __name__ == '__main__':
    test_count = int(input())
    cuts = (int(input()) for _ in range(test_count))

    for k in cuts:
        print(count_pieces(k))
