#!/usr/bin/node
/* This script that fetches the value of the hello key in the url
*/
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('div#hello').text(data.hello);
  });
});
