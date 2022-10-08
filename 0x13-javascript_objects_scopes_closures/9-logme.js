#!/usr/bin/node
exports.logMe = (function (item) {
  let args = 0;
  return function (item) {
    console.log(`${args}: ${item}`);
    args += 1;
  };
})();
