#!/usr/bin/node
const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  let array = args.slice(2);
  array = array.sort();
  const lenArray = array.length;
  console.log(array[lenArray - 2]);
}
