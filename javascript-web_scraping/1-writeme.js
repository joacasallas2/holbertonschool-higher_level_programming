#!/usr/bin/node
// Write a string to a file.
const fs = require('fs');
const args = process.argv;
const len = args.length;
if (len < 4) {
  console.error('usage must be ./1-writeme.js my_file.txt string');
  process.exit(1);
}
const fileName = args[2];
const stringToWrite = args[3];
fs.writeFileSync(fileName, stringToWrite);
