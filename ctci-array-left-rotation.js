#!/usr/bin/env node

// Performs a left rotation on an array.
//
// https://www.hackerrank.com/challenges/ctci-array-left-rotation

'use strict';

const fs = require('fs');

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

function rotLeft(a, d) {
    const rotated = a.slice(0, d);
    const remainder = a.slice(d);
    return remainder.concat(rotated);
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    const nd = readLine().split(' ');
    const n = parseInt(nd[0], 10);
    const d = parseInt(nd[1], 10);
    const a = readLine().split(' ').map(aTemp => parseInt(aTemp, 10));
    const result = rotLeft(a, d);
    ws.write(result.join(' ') + '\n');
    ws.end();
}
