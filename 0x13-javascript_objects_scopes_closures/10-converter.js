#!/usr/bin/node

exports.converter = function (base) {
  return numConver => numConver.toString(base);
};
