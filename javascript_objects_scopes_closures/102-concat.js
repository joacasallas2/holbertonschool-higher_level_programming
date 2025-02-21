#!/usr/bin/node
// Concat 2 files.
const fs = require('fs');
const args = process.argv;
const len = args.length;
if (len < 5) {
  console.error('usage: ./102-concat.js <fileA> <fileB> <fileC>');
  process.exit(1);
}
const fileA = args[2];
const fileB = args[3];
const fileC = args[4];
const contentA = fs.readFileSync(fileA, 'utf8');
const contentB = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, contentA + contentB);
