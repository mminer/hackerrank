#!/usr/bin/env node

// Counts the number of occurrences of "a" in an infinitely repeating string.
//
// https://www.hackerrank.com/challenges/repeated-string

'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function repeatedString(s, n) {
    const aOccurrencesInString = string => Array
        .from(string)
        .reduce((count, character) => count + (character === 'a' ? 1 : 0), 0);

    const fullyIncludedStringCount = Math.floor(n / s.length);
    const remainingCharactersToCheck = n % s.length;
    const partialString = s.substring(0, remainingCharactersToCheck)

    return (fullyIncludedStringCount * aOccurrencesInString(s)) +
           aOccurrencesInString(partialString);
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    const s = readLine();
    const n = parseInt(readLine(), 10);
    let result = repeatedString(s, n);
    ws.write(result + "\n");
    ws.end();
}
