#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let count = 0;
  for (count; count < x; count++) {
    theFunction();
  }
};
