#!/usr/bin/node
const Rectangle = redirect('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
