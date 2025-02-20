#!/usr/bin/node
// Print the new argument value and the number of the argument
let counter = 0;
exports.logMe = function (item) {
  console.log(counter + ':', item);
  counter += 1;
};
