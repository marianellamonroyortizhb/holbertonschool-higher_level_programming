#!/usr/bin/node

const sizing = parseInt(process.argv[2]);

if (parseInt(process.argv[2])) {
  let counter = 0
  for (counter = 0; counter < sizing; counter++) {
    console.log('X'.repeat(sizing));
  }
} else {
  console.log('Missing size');
}
