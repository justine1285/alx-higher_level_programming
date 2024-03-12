#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return this;
    }
    this.width = w;
    this.height = h;
  }

  print () {
   for (let i = 0; i < this.height; i++) {
     let row = '';
     for (let j = 0; j < this.width; j++) {
       row += 'X';
     }
     console.log(row);
   }
  }

  rotate () {
    let temp = 0;
    temp = this.height;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};