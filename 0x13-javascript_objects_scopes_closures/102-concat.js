#!/usr/bin/node
const fs = require('fs');

const sourceFilePath1 = fs.readFileSync(process.argv[2]).toString();
const sourceFilePath2 = fs.readFileSync(process.argv[3]).toString();
const destinationFilePath = process.argv[4];

fs.writeFileSync(destinationFilePath, sourceFilePath1 + sourceFilePath2);
