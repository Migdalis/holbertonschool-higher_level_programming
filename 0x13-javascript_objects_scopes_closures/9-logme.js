#!/usr/bin/node

let numArgPrinted = 0;
exports.logMe = function (item) {
  console.log(numArgPrinted + ': ' + item);
  numArgPrinted++;
};
