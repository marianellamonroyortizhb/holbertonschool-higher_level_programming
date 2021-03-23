#!/usr/bin/node
const InputArg = process.argv;
if (InputArg.length < 3) {
  console.log('No argument');
} else if (InputArg.length === 3){
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
