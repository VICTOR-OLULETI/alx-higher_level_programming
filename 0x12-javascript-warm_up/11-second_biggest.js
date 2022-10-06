#!/usr/bin/node
const args = process.argv.length;
const arr = process.argv;
let second;
let first;
if (args <= 3) {
  second = 0;
} else {
  first = arr[2];
  second = arr[2];
  for (let i = 2; i < args; i++) {
    if (arr[i] >= first) {
      second = first;
      first = arr[i];
    } else if (arr[i] > second) {
      second = arr[i];
    }
  }
}
console.log(`${second}`);
