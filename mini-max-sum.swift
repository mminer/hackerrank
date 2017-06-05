#!/usr/bin/env xcrun swift

// Finds minimum and maximum values calculated by summing exactly four of five supplied integers.
//
// https://www.hackerrank.com/challenges/mini-max-sum

import Foundation

let numbers = readLine()!
    .components(separatedBy: " ")
    .flatMap { Int($0) }
    .sorted()

let minSum = numbers.prefix(4).reduce(0, +)
let maxSum = numbers.suffix(4).reduce(0, +)
print(minSum, maxSum)
