#!/usr/bin/node
/* This script that fetches star wars movie titles
*/
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const results = data.results;
    results.forEach(element => {
      $('ul#list_movies').append('<li>' + element.title + '</li>');
    });
  });
});
