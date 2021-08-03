#!/usr/bin/node
const argum1 = parseInt(process.argv[2]);

function fact (argum1) {
  if (!Number(argum1)) {
    return 1;
  } else if (argum1 !== 0) {
    return (argum1 * fact(argum1 - 1));
  } else if (!Number(argum1)) {
    return 1;
  }
}
console.log(fact(argum1));
