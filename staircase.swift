#!/usr/bin/env xcrun swift

// Prints a staircase of the supplied size.
//
// https://www.hackerrank.com/challenges/compare-the-triplets

import Foundation

let stairCount = Int(readLine()!)!

(1...stairCount)
    .map { stair in
        let characters = String(repeating: "#", count: stair)
            .padding(toLength: stairCount, withPad: " ", startingAt: 0)
            .characters
            .reversed()

        return String(characters)
    }
    .forEach { print($0) }
