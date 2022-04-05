#!/usr/bin/node

let biggest = 0;
let second = 0;
process.argv.forEach((value, index) => {
  const num = Number(value);
  if (num > biggest) {
    second = biggest;
    biggest = num;
  } else if (num < biggest && num > second) {
    second = num;
  }
});

console.log(second);
