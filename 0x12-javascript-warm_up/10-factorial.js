#!/usr/bin/node

const result = factorial(Number(process.argv[2]));
console.log(result);

function factorial (num) {
  let value = 1;
  if (isNan(num) || num == 1) {
    return (1);
  } esle {
    value = num + factorial(num - 1);
    return (value);
  }
}
