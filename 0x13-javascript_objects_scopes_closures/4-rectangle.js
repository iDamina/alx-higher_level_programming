#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (this.isValidDimension(w) && this.isValidDimension(h)) {
      this.width = w;
      this.height = h;
    } else {
      this.width = 0;
      this.height = 0;
    }
  }

  isValidDimension (value) {
    return Number.isInteger(value) && value > 0;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
