#!/usr/bin/env node

// Counts the number of valleys traversed (consecutive elevation dips below 0).
//
// https://www.hackerrank.com/challenges/counting-valleys

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

function countingValleys(n, s) {
    let elevation = 0;
    let valleyCount = 0;

    Array.from(s).forEach(step => {
        switch (step) {
            case 'D': // Downhill
                elevation -= 1;
                break;

            case 'U': // Uphill
                elevation += 1;

                if (elevation === 0) {
                    valleyCount += 1;
                }

                break;
        }
    });

    return valleyCount;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    const n = parseInt(readLine(), 10);
    const s = readLine();
    let result = countingValleys(n, s);
    ws.write(result + "\n");
    ws.end();
}
