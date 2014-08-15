#!/usr/bin/env python

"""
Dtermines if HackerRank API requests contain a valid language.

https://www.hackerrank.com/challenges/hackerrank-language
"""

import re

VALID_LANGUAGES = [
    'BASH', 'BRAINFUCK', 'C', 'CLISP', 'CLOJURE', 'CPP', 'CSHARP', 'D', 'DART',
    'ERLANG', 'GO', 'GROOVY', 'HASKELL', 'JAVA', 'JAVASCRIPT', 'LUA',
    'OBJECTIVEC', 'OCAML', 'PASCAL', 'PERL', 'PHP', 'PYTHON', 'R', 'RUBY',
    'SCALA', 'SBCL',
]


def verify_request_validity(requests):
    """Prints 'VALID' for requests with valid language, 'INVALID' otherwise."""
    pattern = get_pattern()

    for request in requests:
        print('VALID' if pattern.match(request) else 'INVALID')


def get_pattern():
    """Compiles a regex pattern that matches the valid languages."""
    languages = '|'.join(VALID_LANGUAGES)
    regex = '^\d+ ({0})$'.format(languages)
    pattern = re.compile(regex)
    return pattern


if __name__ == '__main__':
    request_count = int(input())
    requests = (input() for _ in range(request_count))
    verify_request_validity(requests)
