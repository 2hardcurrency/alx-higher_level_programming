#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends Square {
  constructor () {
  }
  
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (i = 0; i < this.height; i++) {
      size = '';
      for (j = 0; j < this.width; j++) {
	size += 'c';
      }
      console.log(size);
    }
  }
}

module.exports = Square;
