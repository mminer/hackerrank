#!/usr/bin/env bash
#
# Print "YES" given a 'Y' or 'y', "NO" otherwise.
# https://www.hackerrank.com/challenges/bash-tutorials---getting-started-with-conditionals

read input

if [[ "$input" == 'Y' || "$input" == 'y' ]]; then
    echo 'YES'
else
    echo 'NO'
fi
