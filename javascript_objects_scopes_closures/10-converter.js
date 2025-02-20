#!/usr/bin/node
// Convert a number from base 10 to another base passed as argument
exports.converter = function (base) {
  return function convertNumber (number) {
    return number.toString(base);
  };
};
