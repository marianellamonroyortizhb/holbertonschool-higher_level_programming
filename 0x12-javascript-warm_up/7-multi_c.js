#!/usr/bin/node
let mult;
const Arg1 = parseInt(process.argv[2]);

if (Arg1) {
  for (mult = 1; mult <= Arg1; mult++) {
    console.log('C is Fun');
  }
} else {
  console.log('Missing number of occurrences');
}
