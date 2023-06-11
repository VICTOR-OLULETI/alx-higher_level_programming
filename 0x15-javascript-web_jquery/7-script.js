#!/usr/bin/node
/* This script that fetches the character name from this URL
*/
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    $('div#character').text(data.name);
  });
});
