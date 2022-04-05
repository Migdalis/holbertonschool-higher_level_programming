#!/usr/bin/node

function factorial (num) {
  if (num < 0) {
    return -1;
  } else if (num === 0) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}

if (isNaN(process.argv[2])) {
  console.log(factorial(0));
} else {
  console.log(factorial(parseInt(process.argv[2])));
}
