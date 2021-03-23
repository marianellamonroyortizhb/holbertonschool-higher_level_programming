#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

add(parseInt(arg1), parseInt(arg2));
