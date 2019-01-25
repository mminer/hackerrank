#!/usr/bin/env node

// Counts minimum number of jumps required to traverse array without visiting 1.
//
// https://www.hackerrank.com/challenges/jumping-on-the-clouds

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

function jumpingOnClouds(c) {
    let jumpCount = 0;
    let index = 0;

    while (index < c.length - 1) {
        if (c[index + 2] === 0) {
            index += 2;
        } else {
            index += 1;
        }

        jumpCount += 1;
    }

    return jumpCount;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    const n = parseInt(readLine(), 10);
    const c = readLine().split(' ').map(cTemp => parseInt(cTemp, 10));
    let result = jumpingOnClouds(c);
    ws.write(result + "\n");
    ws.end();
}
