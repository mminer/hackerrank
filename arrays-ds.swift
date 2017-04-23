#!/usr/bin/env xcrun swift

// Prints an array of integers in reverse order on a single line.
//
// https://www.hackerrank.com/challenges/arrays-ds

import Foundation

_ = readLine()

readLine()!
    .components(separatedBy: " ")
    .flatMap { Int($0) }
    .reversed()
    .forEach { print($0, terminator: " ") }
