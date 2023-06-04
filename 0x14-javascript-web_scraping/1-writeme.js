#!/usr/bin/node
/* This script write and prints the content of a file
*/

const fs = require('fs');

function writePrintFile (filePath) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}

/* node script.js <file-path> */
const filePath = process.argv[2];
const content = process.argv[3];
writePrintFile(filePath, content);
