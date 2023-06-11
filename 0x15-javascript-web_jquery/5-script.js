#!/usr/bin/node
/* This script adds a li element to a list when the user clicks on the tag
div#add_item
*/

$('div#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
