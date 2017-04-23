#!/usr/bin/env xcrun swift

// Prints the sum of the array's elements as a single integer.
//
// https://www.hackerrank.com/challenges/simple-array-sum

import Foundation

_ = readLine()

let result = readLine()!
    .components(separatedBy: " ")
    .flatMap { Int($0) }
    .reduce(0, +)

print(result)
