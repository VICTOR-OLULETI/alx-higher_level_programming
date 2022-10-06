#!/usr/bin/node
const arg1 = parseInt(process.argv[2], 10);
const arg2 = parseInt(process.argv[3], 10);

function add (a, b) {
  if (!isNaN(b)) {
    console.log(`${a + b}`);
  } else {
    console.log('NaN');
  }
}
add(arg1, arg2);
