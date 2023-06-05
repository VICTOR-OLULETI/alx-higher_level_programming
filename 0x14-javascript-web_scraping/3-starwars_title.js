#!/usr/bin/node
/* This script prints the title of a Star Wars movie
where the episode number matches a given integer.
*/

const request = require('request');

function movieTitle (url) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (response.statusCode !== 200) {
      console.error(response.statusCode);
    } else {
      const data = JSON.parse(body);
      console.log(data.title);
    }
  });
}

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
movieTitle(url);
