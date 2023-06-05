#!/usr/bin/node
/* This script gets the contents of a webpage and
stores it in a file.
*/
const fs = require('fs');
const request = require('request');
// let content;
function storeInFile (url, filePath) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          console.log(err);
        }
      });
    }
  });
}

// node script <url> <filePath>
const url = process.argv[2];
const filePath = process.argv[3];
storeInFile(url, filePath);
