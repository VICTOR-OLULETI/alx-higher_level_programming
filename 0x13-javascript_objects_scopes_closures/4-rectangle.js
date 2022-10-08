#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let result = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        result += 'X';
      }
      console.log(result);
      result = '';
    }
  }

  rotate () {
    const width = this.width;
    const height = this.height;
    this.height = width;
    this.width = height;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
};
