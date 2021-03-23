#!/usr/bin/node
const inputar = process.argv;
if (inputar.length < 3) {
  console.log('No argument');
} else if (inputar.length === 3){
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
