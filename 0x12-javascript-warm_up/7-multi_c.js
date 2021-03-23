#!/usr/bin/node
let counter;

if (parseInt(process.argv[2])) {
  for (counter = 1; counter <= process.argv[2]; counter++){
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
