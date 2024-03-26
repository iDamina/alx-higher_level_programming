#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  console.log('Usage: node script.js <file_path> <string_to_write>');
  process.exit(1);
}

const filepath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filepath, content, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
