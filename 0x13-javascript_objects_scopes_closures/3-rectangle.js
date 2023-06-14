#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || !Number.isInteger(w) || h <= 0 || !Number.isInteger(h)) {
      return {}; // Return an empty object if width or height is not valid
    }

    this.width = w;
    this.height = h;
  }

  print() {
    if (!this.width || !this.height) {
      console.log("Invalid rectangle"); // Print an error message if width or height is not valid
      return;
    }

    for (let i = 0; i < this.height; i++) {
      console.log("X".repeat(this.width));
    }
  }
}
module.exports = Rectangle
