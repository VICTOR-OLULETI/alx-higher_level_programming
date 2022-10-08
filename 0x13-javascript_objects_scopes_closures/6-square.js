#!/usr/bin/node
const square = require('./5-square');
module.exports = class Square extends square {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    let character = c;
    if (c === undefined) {
      character = 'X';
    }
    let result = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        result += character;
      }
      console.log(result);
      result = '';
    }
  }
};
