#!/usr/bin/node
// Reads and prints the content of a file.
const fs = require('fs');
const args = process.argv;
const len = args.length;
if (len < 3) {
  console.error('usage must be: ./0-readme.js filename');
  process.exit(1);
}
const fileName = args[2];
const content = fs.readFileSync(fileName, 'utf-8');
console.log(content);
