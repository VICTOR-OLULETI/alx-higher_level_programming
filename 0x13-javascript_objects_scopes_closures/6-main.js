#!/usr/bin/node
const Square = require('./6-square');

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');
s1.charPrint('D');
console.log("before:");
console.log(s1);
s1.double()
console.log("after:");
console.log(s1);
s1.charPrint('O');
