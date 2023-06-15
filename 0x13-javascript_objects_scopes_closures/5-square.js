#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
    this.size = size;
  }
}

const square = new square;
console.log(square.getArea());

module.exports = Square;
