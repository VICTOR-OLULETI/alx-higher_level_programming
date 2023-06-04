#!/usr/bin/node
/* This script write the contents to a file
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
