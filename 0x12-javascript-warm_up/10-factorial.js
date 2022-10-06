#!/usr/bin/node
const arg = parseInt(process.argv[2], 10);

function factorial (a) {
  if (a === 1 || a === 0) {
    return (1);
  }
  if (isNaN(a)) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}
console.log(`${factorial(arg)}`);
