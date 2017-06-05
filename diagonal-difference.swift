#!/usr/bin/env xcrun swift

// Calculates absolute difference between the sums of a 2D array's diagonals.
//
// https://www.hackerrank.com/challenges/diagonal-difference

import Foundation

let size = Int(readLine()!)!

let matrix = (1...size).map { _ in
    readLine()!.components(separatedBy: " ").flatMap { Int($0) }
}

let primaryDiagonalSum = (0..<size)
    .map { row in
        let column = row
        return matrix[row][column]
    }
    .reduce(0, +)

let secondaryDiagonalSum = (0..<size)
    .map { row in
        let column = size - row - 1
        return matrix[row][column]
    }
    .reduce(0, +)

let difference = abs(primaryDiagonalSum - secondaryDiagonalSum)
print(difference)
