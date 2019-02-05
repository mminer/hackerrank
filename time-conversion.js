#!/usr/bin/env node

// Converts a 12-hour AM/PM format to military (24-hour) time.
//
// https://www.hackerrank.com/challenges/time-conversion

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
    inputString = inputString.trim().split('\n').map(str => str.trim());
    main();
});

function readLine() {
    return inputString[currentLine++];
}

function timeConversion(s) {
    const regex = /(\d{2}):(\d{2}):(\d{2})(\w{2})/g;
    let [, hours, minutes, seconds, period] = regex.exec(s);

    if (period === 'AM' && hours === '12') {
        hours = '00';
    } else if (period === 'PM' && hours !== '12') {
        hours = (parseInt(hours) + 12).toString();
    }

    return `${hours}:${minutes}:${seconds}`;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    const s = readLine();
    let result = timeConversion(s);
    ws.write(result + "\n");
    ws.end();
}
