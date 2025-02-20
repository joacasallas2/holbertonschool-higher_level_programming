#!/usr/bin/node
// Function that returns the reversed version of a list
exports.esrever = function (list) {
  const listReversed = [];
  const len = list.length;
  for (let i = 0, j = len - 1; i < len; i++, j--) {
    listReversed[i] = list[j];
  }
  return listReversed;
};
