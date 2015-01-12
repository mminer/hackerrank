#!/usr/bin/env bash
#
# Prints the odd numbers between 1 and 99.
# https://www.hackerrank.com/challenges/bash-tutorials---looping-and-skipping

for i in {1..99..2}; do
    echo $i
done
