#!/usr/bin/node

const args = process.argv
  .slice(2)
  .map(Number)
  .filter((n) => !isNaN(n));
const lenArgs = args.length;
if (lenArgs < 2) {
  console.log(0);
} else {
  const argsSorted = [...new Set(args)].sort((a, b) => b - a);
  console.log(argsSorted[1]);
}
