#!/usr/bin/node
/* This script updates the color of the header when a
click occurs
*/

const $header = $('header');
const $red = $('div#red_header');

// Attach a click event handler
$red.click(function () {
  // Change the header color when clicked
  $header.css('color', '#FF0000');
});
