#!/usr/bin/node
let mult;

if (parseInt(process.argv[2])) {
  for (mult = 1; mult <= process.argv[2]; mult++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
