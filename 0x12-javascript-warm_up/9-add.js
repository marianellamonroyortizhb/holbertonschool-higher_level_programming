#!/usr/bin/node
let res;
const arg1 = process.argv[2];
const arg2 = process.argv[3];

function add (a, b) {
  res = parseInt(arg1) + parseInt(arg2);
  console.log(res);
}

add (arg1, arg2);
