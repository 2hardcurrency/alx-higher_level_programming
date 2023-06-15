#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    super(size, size); // Call the constructor of Rectangle with the size argument
  }
}

// Create a new instance of Square
const square = new Square(5);

console.log(square.area());

module.exports = Square;
