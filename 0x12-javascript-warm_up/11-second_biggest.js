#!/usr/bin/node

const len = process.argv.length - 2;
const array = process.argv.slice(2);

if (len > 1) {
  array.sort((a, b) => {
    return a - b;
  });
  console.log(array[len - 2]);
} else {
  console.log('0');
}
