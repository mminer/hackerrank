#!/usr/bin/env python

"""
Counts the number of elements that appear in all given rocks.

https://www.hackerrank.com/challenges/gem-stones
"""


def count_gem_elements(rocks):
    """Finds the number of 'gem elements' in the given rocks."""
    # Remove duplicate elements by treating the elements in each rock as a set.
    # Finding the intersection of these sets gives us elements in all rocks.
    element_sets = [set(rock) for rock in rocks]
    gem_elements = set.intersection(*element_sets)
    return len(gem_elements)


if __name__ == '__main__':
    rock_count = int(input())
    rocks = (input() for _ in range(rock_count))
    print(count_gem_elements(rocks))
