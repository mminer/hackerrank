#!/usr/bin/env xcrun swift

// Prints the sum of the array's elements, some of which may be very large.
//
// https://www.hackerrank.com/challenges/a-very-big-sum

import Foundation

_ = readLine()

let result = readLine()!
    .components(separatedBy: " ")
    .flatMap { Int($0) }
    .reduce(0, +)

print(result)
