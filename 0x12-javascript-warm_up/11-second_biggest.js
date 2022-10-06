#!/usr/bin/node
const args = process.argv.length;
const arr = process.argv;
let second;
let first;
if (args <= 3) {
  second = 0;
} else {
  first = -100000000;
  second = -100000000;
  for (let i = 2; i < args; i++) {
    if (arr[i] > first) {
      second = first;
      first = arr[i];
    } else if (arr[i] > second && arr[i] !== first) {
      second = arr[i];
    }
  }
}
console.log(`${second}`);
