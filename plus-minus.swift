#!/usr/bin/env xcrun swift

// Calculates which fraction of an integer array's elements are positive, negative, and zero.
//
// https://www.hackerrank.com/challenges/plus-minus

import Foundation

func fraction(of numbers: [Int], where isIncluded: (Int) -> Bool) -> Double {
    let includedNumbers = numbers.filter(isIncluded)
    return Double(includedNumbers.count) / Double(numbers.count)
}

_ = readLine()
let numbers = readLine()!.components(separatedBy: " ").flatMap { Int($0) }
let positive = fraction(of: numbers) { $0 > 0 }
let negative = fraction(of: numbers) { $0 < 0 }
let zero = fraction(of: numbers) { $0 == 0 }
print(positive, negative, zero, separator: "\n")
