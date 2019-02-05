#!/usr/bin/env node

// Finds two values in an array that add up to a given number.
//
// https://www.hackerrank.com/challenges/ctci-ice-cream-parlor

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

function whatFlavors(cost, money) {
    const costMap = cost.reduce((map, value, index) => {
        map[value] = index;
        return map;
    }, {});

    for (let index = 0; index < cost.length; index += 1) {
        const value = cost[index];
        const neededValue = money - value;
        const otherIndex = costMap[neededValue];

        if (otherIndex) {
            console.log(index + 1, otherIndex + 1);
            return;
        }
    }
}

function main() {
    const t = parseInt(readLine(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const money = parseInt(readLine(), 10);
        const n = parseInt(readLine(), 10);
        const cost = readLine().split(' ').map(costTemp => parseInt(costTemp, 10));
        whatFlavors(cost, money);
    }
}
