#!/usr/bin/node
/* This script toggles between the class red and green to change the header color when click occurs on the tag
toggle header
*/

const $toggle = $('#toggle_header');
const $header = $('header');

$toggle.click(function () {
  $header.toggleClass('red green');
});
