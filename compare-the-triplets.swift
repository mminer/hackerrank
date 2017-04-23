#!/usr/bin/env xcrun swift

// Compares two tuples, assigning a point for each element greater than the other.
//
// https://www.hackerrank.com/challenges/compare-the-triplets

import Foundation

let a = readLine()!.components(separatedBy: " ").flatMap { Int($0) }
let b = readLine()!.components(separatedBy: " ").flatMap { Int($0) }
let aScore = zip(a, b).filter(>).count
let bScore = zip(b, a).filter(>).count
print(aScore, bScore)
