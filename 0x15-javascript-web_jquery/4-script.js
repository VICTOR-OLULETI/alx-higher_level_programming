#!/usr/bin/node
/* This script adds the class red to the header when a
click occurs on the tag DIV#red_header
*/

const $toggle = $('#toggle_header');
const $header = $('header');

$toggle.click(function() {
    $header.toggleClass('red green');
})
