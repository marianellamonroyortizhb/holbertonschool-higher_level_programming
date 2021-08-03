#!/usr/bin/node
let iteration = 0;

exports.callMeMoby = function (x, theFunction) {
  for (iteration; iteration < x; iteration++) {
    theFunction();
  }
};
