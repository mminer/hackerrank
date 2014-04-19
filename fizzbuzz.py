#!/usr/bin/env python

"""
Prints numbers 1 to 100.
Prints "Fizz" for multiples of three.
Prints "Buzz" for multiples of five.
Prints "FizzBuzz" for multiples of both three and five.

https://www.hackerrank.com/challenges/fizzbuzz
"""


def fizz_buzz(n=100):
    for i in range(1, n + 1):
        if i % 3 and i % 5:
            print('FizzBuzz')
        elif i % 3:
            print('Fizz')
        elif i % 5:
            print('Buzz')
        else:
            print(i)


if __name__ == '__main__':
    fizz_buzz()
