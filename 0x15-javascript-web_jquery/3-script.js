#!/usr/bin/node
/* This script adds the class red to the header when a
click occurs on the tag DIV#red_header
*/

const $redHeader = $('div#red_header');
const $header = $('header');

$redHeader.click(function () {
  // add a class red when this tag is clicked
  $header.addClass('red');
});
