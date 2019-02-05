#!/usr/bin/env node

// Determines max number of items that can be purchased within a given budget.
//
// https://www.hackerrank.com/challenges/mark-and-toys

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

function maximumToys(prices, k) {
    prices.sort((a, b) => a - b);
    let numberOfToys = 0;
    let total = 0;

    for (let i = 0; i < prices.length; i += 1) {
        const price = prices[i];

        if (total + price > k) {
            break;
        }

        numberOfToys += 1;
        total += price;
    }

    return numberOfToys;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    const nk = readLine().split(' ');
    const n = parseInt(nk[0], 10);
    const k = parseInt(nk[1], 10);
    const prices = readLine().split(' ').map(pricesTemp => parseInt(pricesTemp, 10));
    let result = maximumToys(prices, k);
    ws.write(result + "\n");
    ws.end();
}
