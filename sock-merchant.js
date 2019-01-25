#!/usr/bin/env node

// Returns an integer representing the number of matching pairs of socks.
//
// https://www.hackerrank.com/challenges/sock-merchant

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

function sockMerchant(n, ar) {
    const colorCounts = ar.reduce((map, color) => {
        map[color] = (map[color] || 0) + 1;
        return map;
    }, {});

    return Object
        .values(colorCounts)
        .reduce((pairCount, colorCount) => pairCount + Math.floor(colorCount / 2), 0);
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    const n = parseInt(readLine(), 10);
    const ar = readLine().split(' ').map(arTemp => parseInt(arTemp, 10));
    let result = sockMerchant(n, ar);
    ws.write(result + "\n");
    ws.end();
}
