#!/usr/bin/env node

// Rounds grades up to the nearest multiple of 5 if they're less than 3 away.
//
// https://www.hackerrank.com/challenges/grading

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

function gradingStudents(grades) {
    return grades.map(grade => {
        if (grade < 38) {
            return grade;
        }

        const amountBelowNextMultiple = 5 - (grade % 5);

        if (amountBelowNextMultiple < 3) {
            grade += amountBelowNextMultiple;
        }

        return grade;
    });
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    const n = parseInt(readLine(), 10);
    let grades = [];

    for (let gradesItr = 0; gradesItr < n; gradesItr++) {
        const gradesItem = parseInt(readLine(), 10);
        grades.push(gradesItem);
    }

    let result = gradingStudents(grades);
    ws.write(result.join("\n") + "\n");
    ws.end();
}
