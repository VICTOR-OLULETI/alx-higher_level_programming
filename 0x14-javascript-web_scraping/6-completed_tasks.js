#!/usr/bin/node
/* This script computes the number of tasks completed
by user id */

const request = require('request');
function noTasks (url) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const data = JSON.parse(body);
      const completed = {};
      for (let i = 0; i < data.length; i++) {
        if (data[i].completed) {
          if (data[i].userId in completed) {
            completed[data[i].userId] += 1;
          } else {
            completed[data[i].userId] = 1;
          }
        }
      }
      console.log(completed);
    }
  });
}

// node script.js <url>
const url = process.argv[2];
noTasks(url);
