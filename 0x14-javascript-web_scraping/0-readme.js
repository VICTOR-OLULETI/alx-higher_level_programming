#!/usr/bin/node
/* This script reads and prints the content of a file
*/

const fs = require('fs');

function readPrintFile (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}

/* node script.js <file-path> */
const filePath = process.argv[2];
readPrintFile(filePath);
