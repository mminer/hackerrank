#!/usr/bin/env xcrun swift

// Finds the number of occurrences of the largest value in a given array.
//
// https://www.hackerrank.com/challenges/birthday-cake-candles

import Foundation

_ = readLine()
let numbers = readLine()!.components(separatedBy: " ").flatMap { Int($0) }
let maxNumber = numbers.max()
let occurrences = numbers.filter { $0 == maxNumber }
print(occurrences.count)
