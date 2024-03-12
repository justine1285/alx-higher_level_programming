#!/usr/bin/node

exports.converter = funtion (base) {
  return function convertToBase (number) {
    return number.toString(base);
  };
};
