#!/usr/bin/node
// Import an array and compute a new array.

const { list } = require('./100-data');
const computedList = list.map((x, index) => x * index);
console.log(list);
console.log(computedList);
