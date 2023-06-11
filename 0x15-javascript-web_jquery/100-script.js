#!/usr/bin/node
/* This script updates the text color of the header element to red
*/
document.addEventListener('DOMContentLoaded', function () {
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
});
