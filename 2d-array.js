#!/usr/bin/env node

// Counts the maximum sum of all hourglass patterns in a 2D array.
//
// https://www.hackerrank.com/challenges/2d-array

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

function hourglassSum(arr) {
    let maximumSum = -Infinity;

    for (let y = 1; y < arr.length - 1; y += 1) {
        for (let x = 1; x < arr[0].length - 1; x += 1) {
            const sum = arr[y - 1][x - 1] +
                        arr[y - 1][x] +
                        arr[y - 1][x + 1] +
                        arr[y][x] +
                        arr[y + 1][x - 1] +
                        arr[y + 1][x] +
                        arr[y + 1][x + 1];

            if (sum > maximumSum) {
                maximumSum = sum;
            }
        }
    }

    return maximumSum;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    let arr = Array(6);

    for (let i = 0; i < 6; i++) {
        arr[i] = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }

    let result = hourglassSum(arr);
    ws.write(result + "\n");
    ws.end();
}
