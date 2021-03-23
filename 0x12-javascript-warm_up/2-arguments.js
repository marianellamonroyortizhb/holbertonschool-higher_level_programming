#!/usr/bin/node
const InputArg = process.argv;
let res;
if (InputArg.length < 3) {
	res = 'No argument';
}
else if (InputArg.length === 3){
	res = 'Argument found';
}
else {
	res = 'Arguments found';
}
console.log(res);
