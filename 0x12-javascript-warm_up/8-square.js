#!/usr/bin/node
let mult;

if (parseInt(process.argv[2])) {
  for (mult = 1; mult <= process.argv[2]; mult++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
} else {
  console.log('Missing size');
}
