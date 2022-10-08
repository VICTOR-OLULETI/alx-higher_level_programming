#!/usr/bin/node
const fs = require('fs');
const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];

console.log(`${file1}`);
fs.readFile(`${file1}`, 'utf8', readingFile);
fs.readFile(`${file2}`, 'utf8', readingFile);
function readingFile (error, data) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(`${file3}`, data, { encoding: 'utf8', flag: 'a+' }, writeFile);
  /* fs.writeFile(`${file3}`, '\n', {encoding: "utf8", flag:"a+"}, writeFile);
  */
}
/*
function readingFile2(error, data) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(`${file3}`, data, {encoding: "utf8", flag:"a+"}, writeFile);
};
*/
function writeFile (err) {
  if (err) {
    console.log(err);
  }
}
