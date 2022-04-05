#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = process.argv[2];
  for (let i = 0; i < x; i++) {
    console.log('x'.repeat(x));
  }
}
