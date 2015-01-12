#!/usr/bin/env bash
#
# Given two integers, finds their sum, difference, product and quotient.
# https://www.hackerrank.com/challenges/bash-tutorials---the-world-of-numbers

read X
read Y

echo "$(( $X + $Y ))"
echo "$(( $X - $Y ))"
echo "$(( $X * $Y ))"
echo "$(( $X / $Y ))"
