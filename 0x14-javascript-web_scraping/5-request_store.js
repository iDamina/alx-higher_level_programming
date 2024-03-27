#!/usr/bin/node

const fs = require('fs');
const request = require('request');

if (process.argv.length !== 4) {
  console.log('Usage: node script.js <URL> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
