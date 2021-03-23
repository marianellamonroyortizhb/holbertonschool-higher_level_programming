#!/usr/bin/node

let arginput = process.argv[2];
arginput
if (arginput == null) {
  console.log('No argument');
} else {
  console.log(arginput);
}
