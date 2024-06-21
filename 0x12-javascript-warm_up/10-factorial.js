#!/usr/bin/node
const n = +process.argv[2];
let f = 1;
if (n) {
  for (let i = 1; i <= n; i++) {
    f = f * i;
  }
  console.log(f);
} else {
  console.log(f);
}
