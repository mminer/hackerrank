#!/usr/bin/env bash
#
# Evaluates a given numerical expression to three decimal places.
# https://www.hackerrank.com/challenges/bash-tutorials---arithmetic-operations

read input
printf "%.3f\n" `echo "$input" | bc -l`
