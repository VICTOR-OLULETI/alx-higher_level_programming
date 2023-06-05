#!/usr/bin/node
/* This script prints out the number of movies
where the character Wedge Antilles is present
*/

const request = require('request');

function movieNo (url) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const data = JSON.parse(body).results;
      let count = 0;
      for (let i = 0; i < data.length; i++) {
        const wedgeAntilles = 'https://swapi-api.alx-tools.com/api/people/18/';
        if (data[i].characters.includes(wedgeAntilles)) {
          count++;
        }
      }
      console.log(count);
    }
  });
}

/* node script.js <url> */
const url = process.argv[2];
movieNo(url);
