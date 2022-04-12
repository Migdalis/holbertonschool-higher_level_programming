#!/usr/bin/node

const file = require('fs');

file.readFile(process.argv[2], 'utf8', (error, data) => {
  if (error) {
    return console.log(error);
  }
  console.log(data);
});
