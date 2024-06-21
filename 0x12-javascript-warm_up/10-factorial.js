#!/usr/bin/node
const n = +process.argv[2];
function factorial (n) {
  if (n) {
    return (n * factorial(n - 1));
  } else {
    return (1);
  }
}
console.log(factorial(n));
