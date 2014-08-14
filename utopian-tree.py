#!/usr/bin/env python

"""
Finds the height of a "Utopian tree" after some number of growth cycles.

https://www.hackerrank.com/challenges/utopian-tree
"""

from itertools import cycle, islice


def calculate_height(cycle_count):
    """Determines the height of a tree given number of cycles that passed."""
    growths = cycle([lambda x: x * 2, lambda x: x + 1])
    height = 1

    for growth in islice(growths, cycle_count):
        height = growth(height)

    return height


if __name__ == '__main__':
    tree_count = int(input())

    for _ in range(tree_count):
        cycle_count = int(input())
        print(calculate_height(cycle_count))
