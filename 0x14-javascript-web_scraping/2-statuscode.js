#!/usr/bin/node
/* This script takes in a url and displays
    its status code
*/

const request = require('request');

function getStatusCode (url) {
  request.get(url, (error, response) => {
    if (error) {
      console.log(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

// Usage: script.js <url>
const url = process.argv[2];
getStatusCode(url);
