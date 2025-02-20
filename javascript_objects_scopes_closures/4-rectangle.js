#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w !== 'number' || typeof h !== 'number' || w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const aux = this.height;
    this.height = this.width;
    this.width = aux;
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
