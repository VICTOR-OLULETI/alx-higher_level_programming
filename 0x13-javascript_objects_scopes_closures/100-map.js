#!/usr/bin/node
const list = require('./100-data.js').list;
const list2 = list.map((x, index) => index * x);
console.log(list);
console.log(list2);
