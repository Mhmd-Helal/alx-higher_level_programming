#!/usr/bin/node
const firstIntger = +process.argv[2];
const secondIntger = +process.argv[3];
function add (a, b) {
  console.log(a + b);
}
add(firstIntger, secondIntger);
