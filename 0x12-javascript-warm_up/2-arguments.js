#!/usr/bin/node
const argc = process.argv.length;
console.log(argc);
if (argc === 2) {
  console.log('No argument');
} else if (argc === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
