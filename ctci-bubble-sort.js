#!/usr/bin/env node

// Performs a bubble sort, counting the number of swaps made.
//
// https://www.hackerrank.com/challenges/ctci-bubble-sort

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the countSwaps function below.
function countSwaps(a) {
    let swapCount = 0;

    for (let i = 0; i < a.length; i += 1) {
        for (let j = 0; j < a.length - 1; j += 1) {
            const numberA = a[j];
            const numberB = a[j + 1];

            if (numberA > numberB) {
                a[j] = numberB;
                a[j + 1] = numberA;
                swapCount += 1;
            }
        }
    }

    console.log(`Array is sorted in ${swapCount} swaps.`);
    console.log('First Element:', a[0]);
    console.log('Last Element:', a[a.length - 1]);
}

function main() {
    const n = parseInt(readLine(), 10);
    const a = readLine().split(' ').map(aTemp => parseInt(aTemp, 10));
    countSwaps(a);
}
