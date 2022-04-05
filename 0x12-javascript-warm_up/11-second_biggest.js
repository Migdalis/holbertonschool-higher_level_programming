#!/usr/bin/node

let biggest = 0;
let i = 0;
process.argv.forEach((value, index) => {
  if (parseInt(value) > biggest) {
    biggest = parseInt(value);
  }
  i++;
});
if (i === 3) {
  console.log(0);
} else {
  console.log(biggest);
}
