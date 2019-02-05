#!/usr/bin/env node

// Determines whether two strings share a common substring.
//
// https://www.hackerrank.com/challenges/two-strings

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

function twoStrings(s1, s2) {
    const s1Set = new Set(s1);
    const s2Set = new Set(s2);
    return Array.from(s1Set).some(character => s2Set.has(character)) ? 'YES' : 'NO';
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    const q = parseInt(readLine(), 10);

    for (let qItr = 0; qItr < q; qItr++) {
        const s1 = readLine();
        const s2 = readLine();
        let result = twoStrings(s1, s2);
        ws.write(result + "\n");
    }

    ws.end();
}
