#!/usr/bin/node
/* This script adds, removes and clears li elements from a list
    when the user clicks
*/

$(document).ready(function () {
  const addItem = $('div#add_item');
  addItem.click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  const removeItem = $('div#remove_item');
  removeItem.click(function () {
    $('ul.my_list li').last().remove();
  });
  const clearList = $('div#clear_list');
  clearList.click(function () {
    $('ul.my_list li').remove();
  });
});
