#!/usr/bin/env python

"""
Print numbers 1 to 100. For multiples of three print "Fizz". For multiples of
five print "Buzz". For numbers which are multiples of both three and five print
"FizzBuzz".

https://www.hackerrank.com/challenges/fizzbuzz
"""


def fizz_buzz(n=100):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


if __name__ == '__main__':
    fizz_buzz()
