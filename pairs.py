#!/usr/bin/env python

"""
Given N integers, counts total pairs of integers with a difference of K.

https://www.hackerrank.com/challenges/pairs
"""


def find_pairs_count(numbers, k):
    """Finds how many pairs of numbers have a difference of k."""
    answer = 0
    distinct = set(numbers)

    for number in numbers:
        difference = number - k

        if difference in distinct:
            answer += 1

    return answer


def numbers_from_input():
    """Reads a list of integers from sdtin."""
    tokens = input().split()
    numbers = list(map(int, tokens))
    return numbers


if __name__ == '__main__':
    n, k = numbers_from_input()
    numbers = numbers_from_input()
    pairs_count = find_pairs_count(numbers, k)
    print(pairs_count)
