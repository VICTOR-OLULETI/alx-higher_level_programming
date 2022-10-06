#!/usr/bin/node
const size = parseInt(process.argv[2], 10);
let result = '';
if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      result += 'X';
    }
    console.log(result);
    result = '';
  }
} else {
  console.log('Missing size');
}
