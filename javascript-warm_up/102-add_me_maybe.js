#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  number = parseInt(number) + 1;
  theFunction(number);
};
