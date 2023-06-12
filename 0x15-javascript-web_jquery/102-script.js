#!/usr/bin/node
/* This script fetches and prints how to say "Hello"
depending on the language
*/

$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const lang = $('input#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;
    $.get(url, function (data) {
      $('div#hello').text(data.hello);
    });
  });
});
