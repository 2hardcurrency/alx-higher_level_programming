#!/usr/bin/node
exports.converter = function (base) {
  return function convertNumber (number) {
    if (number === 0) {
      return '0';
    }

    let result = 0;
    let remainder;

    while (number !== 0) {
      remainder = number % base;
      result = remainder.toString() + result;
      number = Math.floor(number / base);
    }

    return result;
  };
};
