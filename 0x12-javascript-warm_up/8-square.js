#!/usr/bin/node
const sizeSquare = +process.argv[2];
if (sizeSquare) {
  for (let i = 0; i < sizeSquare; i++) {
    let sympol = '';
    for (let j = 0; j < sizeSquare; j++) {
      sympol += 'X';
    }
    console.log(sympol);
  }
} else {
  console.log('Missing size');
}
