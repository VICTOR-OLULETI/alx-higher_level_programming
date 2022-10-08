#!/usr/bin/node
const dict = require('./101-data').dict;

const order = {};
for (const element of Object.keys(dict)) {
  if (order[dict[element]]) {
    order[dict[element]].push(element);
  } else {
    order[dict[element]] = [element];
  }
}
console.log(order);
