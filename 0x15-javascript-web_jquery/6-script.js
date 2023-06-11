#!/usr/bin/node
/* This script updates the text of the <header> element to
New Header!!! when the user clicks on DIV#update_header
*/

$('div#update_header').click(function () {
  // Updates the text content of the header element
  $('header').text('New Header!!!');
});
