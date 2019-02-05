#!/usr/bin/env node

// Determines whether a message can be created using a given list of words.
//
// https://www.hackerrank.com/challenges/ctci-ransom-note

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

function checkMagazine(magazine, note) {
    const wordMap = magazine.reduce((map, word) => {
        map[word] = (map[word] || 0) + 1;
        return map;
    }, {});

    for (const word of note) {
        if (!wordMap[word]) {
            console.log('No');
            return;
        }

        wordMap[word] -= 1;
    }

    console.log('Yes');
}

function main() {
    const mn = readLine().split(' ');
    const m = parseInt(mn[0], 10);
    const n = parseInt(mn[1], 10);
    const magazine = readLine().split(' ');
    const note = readLine().split(' ');
    checkMagazine(magazine, note);
}
